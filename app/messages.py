from pyfiglet import figlet_format
from simple_chalk import chalk, green, yellow, blue, red
from inquirer import list_input, Path

def welcomeMsg()->None:
    print(figlet_format('MusiCLI', font='isometric3',justify='left', width=240))
    print(chalk.yellow('\nWelcome to MusiCLI, the Command Line Interface that allows you to easily download your music playlists into csv or excel files!'))
    print(chalk.yellow('Here, you also have the option to load songs inside existing files into new playlists. \U0001F601 \n'))

    print(chalk.yellow('Brought to you by Sam. You can find me right here: '), chalk.green('https://github.com/Sam-Mobed/ \n'))

def displayInqList(question:str, options: list[str])->str:
    return list_input(question, choices=options)

def actionList()->str:
    return displayInqList('What would you like to do? ', ['Download an album or a playlist into a file' ,'Upload the songs inside a file to a playlist', 'Help', 'Exit'])

def spotify_download()->str:
    return displayInqList('Would you like to download an album or a user\'s playlist? Note that you need the user\'s credentials in order to access their private playlists.', ['An album' ,'A user\'s playlist', 'Help', 'Return','Exit'])

def getfilePath()->str:
    #has built in validation for path, unlike simple text input
    return Path('music_file', message='Where is the csv/excel file located? ', path_type=Path.FILE)

def gettingAuthorization()->None:
    print(chalk.red('Note that downloading or uploading songs from/to private playlists requires you to authenticate yourself. This process only has to be done once;\n \
                    If  you ever wish to remove authorization from this app, you can simply do so from within your Spotify account.'))

def goodByeMsg()->None:
    print(chalk.blue('Thank you for trying the app, have a good day! \U0001F600'))

def helpMsg()->None:
    print(
        chalk.blue(
        'The usage of this app is rather strightforward. You have two options:\n - Download a playlist from the platform of your choice into a csv/excel file.\n - Upload a playlist to a music streaming platform by providing a path to a csv/excel file.'
        )
    )
    print(
        chalk.blue(
        'You can choose the type of the file, but make sure that the data is organized properly.'
        )
    )
    print(
        chalk.blue(
        'For either option, you need to have an account for the appropriate music streaming platform, as authentication is required to access the playlists.'
        )
    )
    print(
        chalk.blue(
        'You need to make sure that the files containing the songs have the appropriate format of `song_name,artist_name,album_name`, otherwise the script won\'t be able to parse the file properly. \n You will be notified in case a value is missing or the format isn\'t respected'
        )
    )
    print(
        chalk.blue(
        'Some songs that you try to upload to the new playlist may not be available on that platform. Sadly, there is nothing to do about this, but you will be notified if this is the case.\n'
        )
    )