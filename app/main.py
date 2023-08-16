from messages import welcomeMsg,goodByeMsg,actionList,platformList,helpMsg,spotify_download
from sys import exit

def endProgram()->None:
    goodByeMsg()
    exit(0)

def spotfifyDownlaod()->None:
    choice = spotify_download()
    while True:
        if choice=='Return':
            break
        elif choice=='An album':
            pass
        elif choice=='A user\'s playlist':
            pass
        else:
            endProgram()


def download()->None:
    choice = platformList()
    while True:
        if choice=='Return':
            break
        elif choice=='Spotify':
            spotfifyDownlaod()
        elif choice=='Apple Music':
            pass
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
            pass

    endProgram()

if (__name__ == '__main__'):
    run()
    