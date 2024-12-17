
import json, sys
import questionary as quest
from shutil import copy as backup, get_terminal_size as termsize
from rich.console import Console
from typing import Final as Const
from os import system

console: Console = Console() # init the Console

stdout = print # set the func Stdout as print()
stdin = input # set the func Stdin as print()
print = console.print # set the func Print as console.print()
input = console.input # set the func Input as console.input()
clear = console.clear # set the func Clear as console.clear()


