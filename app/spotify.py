from dotenv import load_dotenv
from os import getenv
from typing import Tuple
from base64 import b64encode
from requests import post,get
from json import loads

def loadEnvVars()->Tuple[str,str]:
    load_dotenv()

    spotify_client_id = getenv("CLIENT_ID_SPOTIFY")
    spotify_client_secret = getenv("CLIENT_SECRET_SPOTIFY")

    return spotify_client_id, spotify_client_secret

#we need to create an authorization string, that we encode in base 64
#this entails concatinating our client id and client secret, and then encode it.
def get_token()->str:
    id,secret = loadEnvVars()
    auth_string = f"{id}:{secret}"
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type":  "application/x-www-form-urlencoded"
    }

    data = {"grant_type": "client_credentials"}
    result = post(url,headers=headers,data=data)

    json_result = loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token:str)->dict:
    return {"Authorization": "Bearer " + token}

def search_album(token:str, artist:str, album_name:str):
    url = 'https://api.spotify.com/v1/search'
    headers = get_auth_header(token)
    query = f"?q=album:{album_name}%20artist:{artist}&type=album&limit=1"

    query_url = url+query
    result = get(query_url, headers=headers)
    json_result = loads(result.content)

    if 'albums' in json_result and 'items' in json_result['albums'] and len(json_result['albums']['items']) > 0:
        album_id = json_result['albums']['items'][0]['id']
        return album_id

    return None

def get_album_tracks(token:str, id:str):
    url = f'https://api.spotify.com/v1/albums/{id}/tracks'
    headers = get_auth_header(token)

    result = get(url, headers=headers)
    json_result = loads(result.content)

    track_names = []
    if 'items' in json_result:
        for track in json_result['items']:
            if 'name' in track:
                track_names.append(track['name'])

    return track_names

def album_results(token:str):
    pass

id = search_album(get_token(),"Drake", "Certified Lover Boy")
tracks = get_album_tracks(get_token(),id)
print(tracks)
#print(x)