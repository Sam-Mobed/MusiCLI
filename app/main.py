from messages import welcomeMsg,goodByeMsg,actionList,helpMsg,spotify_download,gettingAuthorization
from server import start_server
from sys import exit
from spotify import get_authorization_code
import threading

def endProgram()->None:
    goodByeMsg()
    exit(0)


def download()->None:
    choice = spotify_download()
    while True:
        if choice=='Return':
            break
        elif choice=='An album':
            pass
        elif choice=='A user\'s playlist':
            gettingAuthorization()
            get_authorization_code()
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
    