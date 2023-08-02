from messages import welcomeMsg,goodByeMsg,actionList
from sys import exit

def run()->None:
    welcomeMsg()
    while True:
        action = actionList()
        if action=='Exit':
            break

    goodByeMsg()
    exit(0)

if (__name__ == '__main__'):
    run()
    