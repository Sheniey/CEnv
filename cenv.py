
# Imports:      MODULE IMPORTS
import questionary as quest
from rich.console import Console
from rich.syntax import Syntax
from os import system, makedirs as mkdir
from typing import Final as Const
import sys, json, csv
from shutil import copy as backup, get_terminal_size as termsize

# Imports:      LOCAL IMPORTS
# Coming Soon

# Definition:   INIT MODULES
console: Console = Console() # init the Console

# Definition:   ANONYMOUS FUNCTIONS
stdout = print # set the func Stdout as print()
stdin = input # set the func Stdin as print()
print = console.print # set the func Print as console.print()
input = console.input # set the func Input as console.input()
clear = console.clear # set the func Clear as console.clear()

# Definition:   CONST VARIABLES
CONFIG_PATH: Const[str] = './src/config.json'
CONFIG_BACKUP_PATH: Const[str] = './src/backup/.config_backup.json'
LINKS_PATH: Const[str] = './src/content/links.csv'

# Definition:   VARIABLES
# Maybe

# Initialize:   JSON Files 
def init() -> tuple:
    backup(CONFIG_PATH, CONFIG_BACKUP_PATH) # create a Config Backup
    with open(CONFIG_PATH, 'r', encoding='utf-8') as f: # get the JSON Config File
        config = json.load(f)
        if not config or config == {}: # see if the Config File is Empty
            print(f'\n [!] Config Error: | JSON File is Empty!! |... ')
            print(' [*] Using the Config Backup File... ')
            left: bool = quest.confirm(' Continue... ', qmark='[?]').ask()
            clear()
            if left:
                sys.exit(2)
            with open(CONFIG_BACKUP_PATH, 'r', encoding='utf-8') as backupFile:
                configBackup = json.load(backupFile)
                if not configBackup or configBackup == {}: # see if the Config Backup File is Empty
                    print(f"\n [!] Config Error: | Backup JSON File is Empty!! I'm sorry. |... ")
                    print('     - See the Documentation [DOCS.md] at | https://www.github.com/DOCS.md |... \n')
                    sys.exit(2)
                else: # Config Backup File load
                    print(f'\n [*] Config Backup: | Config Backup File is Loading... |... ')
                    config = configBackup
                    system(f'cp {CONFIG_BACKUP_PATH} {CONFIG_PATH}')
                    input('\n [+] Completed!! ')
                    clear()
    with open(config['language']['path'], 'r', encoding='utf-8') as f: # get the JSON Lang File
        lang = json.load(f)
        if not lang or lang == {}: # see if the JSON File is Empty
            sys.exit(2)
            clear()
    return config, lang
config, lang = init()
IDIOM: str = config.get('idiom', 'en') # get the Idiom

# Definition:   FUNCTIONS
def config_panel() -> None:
    """ ::Configuration Panel Part:: """
    
    clear()
    options: list[str] = lang[IDIOM]['config']['options']
    opt: str = quest.select('', '', options).ask() # show Config Options
    clear()
    if opt == options[0]: # change the Language
        idiome: str = quest.select('', config['language']['lang']).ask() # get the available Languages
        IDIOM = idiome

        # set the new Language
        configLines: list[str] = open(CONFIG_PATH, 'r', encoding='utf-8').readlines()
        with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
            for line in configLines:
                if '"idiom":' in line:
                    line: str = line.replace(f'"idiom": "{configLines[configLines.index(line)].strip()}"', f'"idiom": "{IDIOM}"')
                f.write(line)
                
    elif opt == options[0]: # show Version
        print(config['version'])

def environ_panel(db) -> None: # manages the Custom Environments
    """ ::Environment Panel Part:: """
    
    while div.endswith('/'):
        div: str = quest.select(lang[IDIOM]['createNewEnv']['message'], db[div])
    
    # custom Environments of DB
    if div not in db: # exitin' if Area isn't in the DB
        print(lang[IDIOM]['div']['advice'][0], div, lang[IDIOM]['div']['advice'][1])
        return
    clear()
    
    section: list[str] = list(db[div].keys()) # goto Area the DB
    env: str = quest.select('', section).ask() # show the Program Language of DB
    if env not in db[div]: # exitin' if Program Language isn't in the DB
        print(lang[IDIOM]['lang']['advice'][0], env, lang[IDIOM]['lang']['advice'][1])
        return
    clear()
    
    print(f'\n [+] {env}: ') # show the Program Language as header
    options: list[str] = lang[IDIOM]['lang']['options']
    opt: str = quest.select(lang[IDIOM]['lang']['message'], options).ask() # show Language Options
    
    if opt == options[0]: # Execute Environment
        project: str = quest.text(f' Project Name: ', qmark='[+]').ask() # set the Name of Project
        clear()
        mkdir(f'./{project}') # create the Main Project Folder
            
        for dir in db[div][env]['dirs']: # create the Dirs of environment
            mkdir(f'./{project}/{dir}', exist_ok=True)
                
        for file, content in db[div][env]['Files'].items(): # create the Files with its Content of env
            with open( f'./{project}/{file}', 'w', encoding='utf-8') as f:
                f.write(content)
    
    elif opt == options[1]: # View Environmet
        clear()
        print(Syntax(
            json.dumps(db[div][env], ensure_ascii=config['db']['ascii'], indent=config['db']['indent']),
            lexer='json', theme=config['db']['theme'], line_numbers=config['db']['list'], background_color=config['db']['background'])
        ) # show the JSON DB File
        input()

# Function:     MAIN FUNCTION
def main() -> None: # Main Function
    global IDIOM

    with open(config['db']['path'], 'r', encoding='utf-8') as f: # get the JSON DataBase File
        db = json.load(f)
        if not db or db == {}: # see if the DB file is Empty
            print(lang[IDIOM]['error']['FileIsVoidWarning'])
            sys.exit(2)
    
    section: list[str] = lang[IDIOM]['main']['options'] + [f'[yellow]{env_sect}[/]' for env_sect in db.keys()] # show the Main menu
    option: str = quest.select('', section).ask()
    clear()

    if option == lang[IDIOM]['main']['options'][0]: # Exit Option
        sys.exit(0)
    elif option == lang[IDIOM]['main']['options'][1]: # Credits Option
        print(f'\n [*] Custom Environment [CEnv]: | {config['version']}v | ~ Sheñey [José Daniel]') # show the Credits
        print(f' [+] Follow Me: ') # show the link to Follow Me
        print(f'     [-] Youtube    | https://www.youtube.com/  |... ')
        print(f'     [-] GitHub     | https://www.github.com/   |... ')
        print(f"\n  [!] Thanks You!! :v; feel free to share this, just say it's mine pls. ") # en: Thanks for using CENV
        print(f"\n  [!] Gracias!! :v; Siéntete libre de distribuir esto, solo di que es mío pls.") # es: Agradecimientos por usar CENV
        input('         OK?!')
        clear()
        main()
    elif option == lang[IDIOM]['main']['options'][2]: # Config Option
        config_panel()
        clear()
        main()
    elif option == lang[IDIOM]['main']['options'][3]: # New custom environment Option
        opt: str = quest.select(lang[IDIOM]['createNewEnv']['message'], lang[IDIOM]['createNewEnv']['options']).ask() # show NewEnv Options
        clear()
        if opt == lang[IDIOM]['createNewEnv']['options'][0]: # create a New Custom Environment
            area: str = input('\n [+] Program Area: ')
            name: str = input(' [+] Environment Name: ')
            author: str = input(' [+] Author Name: ')
            version: str = input(' [+] Environment Version: ')
            desc: str = input(' [+] Environment Description: ')
            env: str = input(' [+] Runtime Environment: ')
            dirs: list[str] = input(' [+] Directories [assets,assets/icon]: ').split(',')
            files: list[str] = input(' [+] Files [main.py,icon/favicon.ico]: ').split(',')
            request: list[str] = input(' [+] Dependences: ').split(',')
            clear()
        elif opt == lang[IDIOM]['createNewEnv']['options'][1]: # import a Custom Environment
            ...
        elif opt == lang[IDIOM]['createNewEnv']['options'][2]: # export a Custom Environment
            fromEnv: str = db[quest.select('', db.keys()).ask()].keys()
            clear()
            fromEnv: str = quest.select('', fromEnv).ask()
            toEnv: str = input(' [+] Name File To: ')
            exportFile = open(toEnv, 'w')
            exportFile.writelines(json.dumps(db[fromEnv], ensure_ascii=config['db']['ascii'], indent=config['db']['indent']))
        clear()
        main()
    else:
        environ_panel(db, option)
        input()
    clear()
    return

if __name__ == '__main__':
    try: # run Main Function
        main()
        sys.exit(0)
    except FileNotFoundError: # InterruptError Code
        print(lang[IDIOM]['stderr']['FileNotFoundError'])
        with open(config['db']['path'], 'w') as f:
            json.dump(config['db']['bodyDefault'], f, indent=config['db']['bodyDefault'])
    except json.JSONDecodeError: # JSON DB File is void
        print(lang[IDIOM]['stderr']['JSONDecodeError'])
        with open(config['db']['path'], 'w') as f:
            json.dump(config['db']['bodyDefault'], f, indent=config['db']['bodyDefault'])
    except KeyboardInterrupt: # KeyboardInterrupt Code
        print(lang[IDIOM]['stderr']['KeyboardInterrupt'])
    except Exception as e: # another one Errors
        print(lang[IDIOM]['stderr']['Raised'][0], e, lang[IDIOM]['stderr']['Raised'][1])
    finally:
        sys.exit(1)

# _ExitCode 0 : Program Successed
# _ExitCode 1 : General Error
# _ExitCode 2 : Requiered Data
