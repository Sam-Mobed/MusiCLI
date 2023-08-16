from dotenv import load_dotenv
from os import getenv
from typing import Tuple
from base64 import b64encode
from requests import post
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

print(type(get_token()))
