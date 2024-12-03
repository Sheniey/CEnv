
# Imports:      IMPORTS
import curses
import json
from rich.console import Console
from rich.syntax import Syntax
from os import system, name as OS, makedirs as mkdir
from typing import Final as Const
import sys
from shutil import copy as backup

# Definition:   INIT MODULES
console: Console = Console() # init the Console

# Definition:   ANONYMOUS FUNCTIONS
stdout = print # set the func Stdout as print()
stdin = input # set the func Stdin as print()
print = console.print # set the func Print as console.print()
input = console.input # set the func Input as console.input()
clear = console.clear # set the func Clear as console.clear()

# Definition:   CONST VARIABLES
CONFIG_PATH: Const[str] = './config.json'
CONFIG_BACKUP_PATH: Const[str] = './.config_backup.json'
backup(CONFIG_PATH, CONFIG_BACKUP_PATH) # create a Config Backup
with open(CONFIG_PATH, 'r', encoding='utf-8') as f: # get the JSON Config File
    config = json.load(f)
    if not config or config == {}: # see if the Config File is Empty
        print(f'\n [!] Config Error: | JSON File is Empty!! |... ')
        print(' [*] Using the Config Backup File... ')
        left: bool = input(' [?] Continue... [Y/n]: ').upper()
        clear()
        if left == 'N':
            sys.exit(2)
        with open(CONFIG_BACKUP_PATH, 'r', encoding='utf-8') as backupFile:
            configBackup = json.load(backupFile)
            if not configBackup or configBackup == {}: # see if the Config Backup File is Empty
                print(f"\n [!] Config Error: | Backup JSON File is Empty!! I'm sorry. |... ")
                print('     - See the Documentation [DOCS.md] at | https://www.github.com/DOCS.md |... \n')
                sys.close(2)
            else: # Config Backup File load
                print(f'\n [*] Config Backup: | Config Backup File is Loading... |... ')
                config = configBackup
                input('\n [+] Completed!! ')
                clear()

IDIOM: str = config.get('idiom', 'en') # get the Idiom

# Definition:   FUNCTIONS
def draw_menu(stdscr, options: list[str], msg: str, *, medium: bool = False, listing: bool = True) -> str:
    curses.curs_set(0) # init the chars of Curses
    stdscr.keypad(True) # idk :v
    aim: int = 0 # set the Pointer at 0
    
    while True:
        h, w = stdscr.getmaxyx() # get the Height and Width of the Console
        stdscr.addstr(1, w // 2 - len(msg) // 2, msg) # show the Message

        for i, option in enumerate(options): # show the Options
            x = w // 2 - len(option) // 2 if medium else 1
            y = h // 2 - len(options) // 2 + i + 1
            if i == aim:
                stdscr.attron(curses.A_REVERSE)
                stdscr.addstr(y, x, f' [{i + 1}] {option}' if listing else f' {option}')
                stdscr.attroff(curses.A_REVERSE)
            else:
                stdscr.addstr(y, x, f' [{i + 1}] {option}' if listing else f' {option}')

        stdscr.refresh() # refresh the Console
        key = stdscr.getch() # idk :v

        # Move|Set the value of option with the Pointer
        if key in [curses.KEY_UP, chr(0x2191), 119]: # press W|UP?
            if aim > 0:
                aim -= 1 # goto the Up Option
            else:
                aim += len(options) - 1 # goto the Lowest Option

        elif key in [curses.KEY_DOWN, chr(0x2193), curses.KEY_BACKSPACE, chr(0x8), 115]: # press S|SPACE|DOWN?
            if aim < len(options) - 1:
                aim += 1 # goto the Down Option
            else:
                aim -= len(options) - 1 # goto the Highest Option

        elif key in [curses.KEY_ENTER, ord('\n'), curses.KEY_BTAB, chr(0x9)]: # press ENTER|TAB?
            return options[aim]
        
        else: # show the error for Invalid Option
            clear()
            input(config[IDIOM]['menu-invalidOption'])
            clear()
            return draw_menu(options, msg, listing=listing) # try again...

def environment(db, area: str) -> None: # manages the Custom Environments
    # custom Environments of DB
    if area not in db: # exitin' if Area isn't in the DB
        print(config[IDIOM]['area-advice'][0], area, config[IDIOM]['area-advice'][1])
        return
    clear()
    
    section: list[str] = list(db[area].keys()) # goto Area the DB
    env: str = draw_menu(section) # show the Program Language of DB
    if env not in db[area]: # exitin' if Program Language isn't in the DB
        print(config[IDIOM]['lang-advice'][0], env, config[IDIOM]['lang-advice'][1])
        return
    clear()
    
    print(f'\n [+] {env}: ') # show the Program Language as header
    opt: str = draw_menu(config[IDIOM]['lang-options'], config[IDIOM]['lang-msg']) # show Language Options
    
    if opt == config[IDIOM]['lang-options'][0]: # Execute Environment
        project: str = input(f' [+] Project Name: ') # set the Name of Project
        clear()
        mkdir(f'./{project}') # create the Main Project Folder
            
        for dir in db[area][env]['Dirs']: # create the Dirs of environment
            mkdir(f'./{project}/{dir}', exist_ok=True)
                
        for file, content in db[area][env]['Files'].items(): # create the Files with its Content of env
            with open( f'./{project}/{file}', 'w', encoding='utf-8') as f:
                f.write(content)
    elif opt == config[IDIOM]['lang-options'][1]: # View Environmet
        clear()
        print(Syntax(
            json.dumps(db[area][env], ensure_ascii=config['db']['ascii'], indent=config['db']['indent']),
            lexer='json', theme=config['db']['theme'], line_numbers=config['db']['enlist'], background_color=config['db']['background'])
        ) # show the JSON DB File
        input()

# Function:     MAIN FUNCTION
def main() -> None: # Main Function
    global IDIOM
    
    with open(config['db']['path'], 'r', encoding='utf-8') as f: # get the JSON DataBase File
        db = json.load(f)
        if not db or db == {}: # see if the DB file is Empty
            print(config[IDIOM]['error']['FileIsVoidWarning'])
            sys.close(2)
    
    section: list[str] = config[IDIOM]['main-options'] + list(db.keys()) # show the Main menu
    option: str = draw_menu(section)
    
    if option == config[IDIOM]['main-options'][0]: # Exit Option
        sys.exit(0)
    elif option == config[IDIOM]['main-options'][1]: # Credits Option
        clear()
        print(f'\n [*] Custom Environment [CEnv]: | {config['version']}v | ~ Sheñey [José Daniel]') # show the Credits
        print(f' [+] Follow Me: ') # show the link to Follow Me
        print(f'     [-] Youtube    | https://www.youtube.com/  |... ')
        print(f'     [-] GitHub     | https://www.github.com/   |... ')
        print(f"\n  [!] Thanks You!! :v; feel free to share this, just say it's mine pls. ") # en: Thanks for using CENV
        print(f"\n  [!] Gracias!! :v; Siéntete libre de distribuir esto, solo di que es mío pls.") # es: Agradecimientos por usar CENV
        input('         OK?!')
        clear()
        main()
    elif option == config[IDIOM]['main-options'][2]: # Config Option
        clear()
        opt: str = draw_menu(config[IDIOM]['config-options']) # show Config Options
        clear()
        if opt == config[IDIOM]['config-options'][0]: # change Idiom
            idiome: str = draw_menu(config['lang']) # get the available Languages
            IDIOM = idiome

            # set the new Language
            configLines: list[str] = open(CONFIG_PATH, 'r', encoding='utf-8').readlines()
            with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
                for line in configLines:
                    if '"idiom":' in line:
                        line: str = line.replace(f'"idiom": "{configLines[configLines.index(line)].strip()}"', f'"idiom": "{IDIOM}"')
                    f.write(line)
        clear()
        main()
    elif option == config[IDIOM]['main-options'][3]: # New custom environment Option
        clear()
        opt: str = draw_menu(config[IDIOM]['newenv-options']) # show NewEnv Options
        clear()
        if opt == config[IDIOM]['newenv-options'][0]: # create a New Custom Environment
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
        elif opt == config[IDIOM]['newenv-options'][1]: # import a Custom Environment
            ...
        elif opt == config[IDIOM]['newenv-options'][2]: # export a Custom Environment
            fromEnv: str = db[draw_menu(db.keys())].keys()
            clear()
            fromEnv: str = draw_menu(fromEnv)
            toEnv: str = input(' [+] Name File To: ')
            exportFile = open(toEnv, 'w')
            exportFile.writelines(json.dumps(db[fromEnv], ensure_ascii=config['db']['ascii'], indent=config['db']['indent']))
        clear()
        main()
    else:
        clear()
        environment(db, option)
        input()

    clear()
    return

if __name__ == '__main__':
    try: # run Main Function
        main()
        sys.exit(0)
    except FileNotFoundError: # InterruptError Code
        print(config[IDIOM]['error']['FileNotFoundError'])
        with open(config['db']['path'], 'w') as f:
            json.dump(config['db']['body'], f, indent=config['db']['body'])
    except json.JSONDecodeError: # JSON DB File is void
        print(config[IDIOM]['error']['JSONDecodeError'])
        with open(config['db']['path'], 'w') as f:
            json.dump(config['db']['body'], f, indent=config['db']['body'])
    except KeyboardInterrupt: # KeyboardInterrupt Code
        print(config[IDIOM]['error']['KeyboardInterrupt'])
    except Exception as e: # another one Errors
        print(config[IDIOM]['error']['Raised'][0], e, config[IDIOM]['error']['Raised'][1])
    finally:
        sys.exit(1)

# _ExitCode 0 : Program Successed
# _ExitCode 1 : General Error
# _ExitCode 2 : Requiered Data
