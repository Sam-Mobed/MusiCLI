from messages import welcomeMsg,goodByeMsg,actionList,helpMsg,spotify_download,getPublicPlaylistURL
from server import start_server
from sys import exit
from spotify import get_authorization_code,get_playlist_id,get_client_token,get_playlist_tracks,getUserPlaylists
import threading

def endProgram()->None:
    goodByeMsg()
    exit(0)


def download()->None:
    choice = spotify_download()
    while True:
        if choice=='Return':
            return
        elif choice=='An album':
            pass
        elif choice=='A public playlist':
            playlist_link = getPublicPlaylistURL()
            token = get_client_token()
            #ask for the format of the file
            #ask for the location where he wants to store the file.
            print(get_playlist_tracks(get_playlist_id(playlist_link),token))
            #break out of the current loop, call another function
            return
        elif choice=='A user\'s playlist':
            get_authorization_code()
            return
        elif choice=='Help':
            helpMsg()
            choice = spotify_download()
        else:
            endProgram()
    
def run()->None:
    welcomeMsg()
    while True:
        action = actionList()
        if action=='Exit':
            break
        elif action=='Help':
            helpMsg()
        elif action=='Download an album or a playlist into a file':
            download()
        else:
            #messages to upload csv or excel file.
            pass

    endProgram()

if (__name__ == '__main__'):
    server_thread = threading.Thread(target=start_server)
    server_thread.daemon = True
    server_thread.start()
    run()
    