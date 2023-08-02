from pyfiglet import figlet_format
from simple_chalk import chalk, green, yellow, blue
from inquirer import list_input 

def welcomeMsg()->None:
    print(figlet_format('MusiCLI', font='isometric3',justify='left', width=240))
    print(chalk.yellow('\nWelcome to MusiCLI, the Command Line Interface that allows you to easily download your music playlists into csv or excel files!'))
    print(chalk.yellow('Here, you also have the option to load songs inside existing files into new playlists. \U0001F601 \n'))

    print(chalk.yellow('Brought to you by Sam. You can find me right here: '), chalk.green('https://github.com/Sam-Mobed/ \n'))

def displayInqList(question:str, options: list[str])->str:
    return list_input(question, choices=options)

def actionList()->str:
    return displayInqList('What would you like to do? ', ['Download a playlist into a file', 'Upload the songs inside a file to a playlist', 'Exit'])

def goodByeMsg()->None:
    print(chalk.blue('Thank you for trying the app, have a good day! \U0001F600'))