from messages import welcomeMsg,goodByeMsg,actionList,platformList,helpMsg
from sys import exit

def run()->None:
    welcomeMsg()
    while True:
        action = actionList()
        if action=='Exit':
            break
        elif action=='Help':
            helpMsg()
        elif action=='Download a playlist into a file':
            choice = platformList()
            if choice=='Return':
                pass
            elif choice=='Spotify':
                pass
            elif choice=='Apple Music':
                pass
            else:
                pass
        else:
            pass
            


    goodByeMsg()
    exit(0)

if (__name__ == '__main__'):
    run()
    