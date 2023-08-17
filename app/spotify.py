from dotenv import load_dotenv
from os import getenv
from typing import Tuple
from base64 import b64encode
from requests import post,get
from json import loads
from webbrowser import open

redirect_uri = 'http://localhost:3000/callback'
USER_AUTH_TOKEN = None

def loadEnvVars()->Tuple[str,str]:
    load_dotenv()

    spotify_client_id = getenv("CLIENT_ID_SPOTIFY")
    spotify_client_secret = getenv("CLIENT_SECRET_SPOTIFY")

    return spotify_client_id, spotify_client_secret



#we need to create an authorization string, that we encode in base 64
#this entails concatinating our client id and client secret, and then encode it.
#this token does not give access to user information
def get_client_token()->str:
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

#this functions returns another type of access token; one with which we will
#be able to access user information
def get_authorization_code()->None:
    #build the URL where user will login.
    id = loadEnvVars()[0]
    url = 'https://accounts.spotify.com/authorize'
    scopes = 'playlist-modify-private,playlist-modify-public,user-library-modify,user-library-read,playlist-read-private'
    query=f'?client_id={id}&response_type=code&redirect_uri={redirect_uri}&scope={scopes}'

    auth_url = url + query
    open(auth_url)

def get_authorization_token(code:str)->str:
    global USER_AUTH_TOKEN
    id,secret = loadEnvVars()
    auth_string = f"{id}:{secret}"
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"

    headers = {
        "Authorization": "Basic " + auth_base64,
    }

    data = {
        "code": code,
        "redirect_uri": redirect_uri,
        "grant_type": "authorization_code"
    }

    result = post(url,headers=headers,data=data)

    json_result = loads(result.content)
    token = json_result["access_token"]
    USER_AUTH_TOKEN = token

def get_auth_header(token:str)->dict:
    return {"Authorization": "Bearer " + token}

def get_playlist_tracks(id:str,token:str):
    url = f'https://api.spotify.com/v1/playlists/{id}/tracks'
    query = '?fields=items%28track%28name%2Cartists%28name%29%2Calbum%28name%29%29%29'
    query_url = url+query
    headers = get_auth_header(token)

    result = get(query_url, headers=headers)
    json_result = loads(result.content)
    
    tracks = []
    if 'items' in json_result:
        for track_info in json_result['items']:
            song=track_info['track']['name']
            artist=track_info['track']['artists'][0]['name']
            album=track_info['track']['album']['name']
            tracks.append([song,artist,album])

    return tracks

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

def get_playlist_id(link:str)->str:
    parse1 = link.split('/')[-1]
    id = parse1.split('?')[0]
    return id

#id = search_album(get_client_token(),"Drake", "Certified Lover Boy")
#tracks = get_album_tracks(get_client_token(),id)
#print(tracks)

token = get_client_token()
#id = search_public_playlist(token, "Japanese Lofi HipHop", "thebootlegboy")
id = get_playlist_id('https://open.spotify.com/playlist/37i9dQZF1DWTypZHlgEy1G?si=e2cff0697d8d4237')
tracks = get_playlist_tracks(id,token)
print(tracks)
print(len(tracks))

#print(get_playlist_tracks(id,token))


'''
def getLikedSongs():
    global USER_AUTH_TOKEN
    url = 'https://api.spotify.com/v1/me/tracks'
    #query = '?offset=0&limit=10'
    #url = 'https://api.spotify.com/v1/me/playlists'
    if not USER_AUTH_TOKEN:
        print('Error')
        return
    headers = get_auth_header(USER_AUTH_TOKEN)

    #url_query = url+query
    #print(url_query)
    result = get(url, headers=headers)
    json_result = loads(result.content)
    return json_result

    def getLikedSongs():
    global USER_AUTH_TOKEN
    url = 'https://api.spotify.com/v1/me/playlists'
    headers = get_auth_header(USER_AUTH_TOKEN)

    result = get(url, headers=headers)
    print(result)
    return
    playlists_data = loads(result.content)
    print(playlists_data)
    liked_songs_playlist_id = None

    for playlist in playlists_data['items']:
        if playlist['name'] == 'Liked Songs':
            liked_songs_playlist_id = playlist['id']
            break

    if liked_songs_playlist_id:
        liked_songs_url = f'https://api.spotify.com/v1/playlists/{liked_songs_playlist_id}/tracks'
        result = get(liked_songs_url, headers=headers)
        liked_songs_data = loads(result.content)
        return liked_songs_data['items']
    else:
        print("Liked Songs playlist not found.")
        return []

    '''