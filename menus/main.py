import os 
import subprocess 
import rich #type: ignore
from rich.align import Align #type: ignore
from rich.panel import Panel #type: ignore
from rich.text import Text #type: ignore
from rich.table import Table #type: ignore
from colorama import Fore #type: ignore
import shutil
from rich.box import SIMPLE_HEAVY
from rich.console import Console
console = Console ()
import shutil
my_logo = r"""
                                                                                                                                 
                          _____                                    
  _____  ______      _____\    \     _____       _____             
 /    / /     /|    /    / |    |  /      |_    |\    \            
|     |/ ----/ |   /    /  /___/| / --------\    \\----\           
|\____\\    / /   |    |__ |___|/|     /\    \    \\    \          
 \|___|/   / /    |       \      |    |  |    \    \|    | ______  
    /     /_/____ |     __/ __   |     \/      \    |    |/      \ 
   /     /\      ||\    \  /  \  |\      /\     \   /            | 
  /_____/ /_____/|| \____\/    | | \_____\ \_____\ /_____/\_____/| 
  |====|/|=====| || |====|____/| | |=====| |======|======| |====|| 
  |====| |=====|/  \|====|===| |  \|=====|\|======|======|/|====|/ 
                         |===|/                                    
                                
                                                                                                                                
      """
colors = [
    "\033[31m",  # red
    "\033[33m",  # yellow
    "\033[32m",  # green
    "\033[36m",  # cyan
    "\033[34m",  # blue
    "\033[35m",  # magenta
    "\033[37m",  # white
    "\033[91m",  # bright red
    "\033[94m",  # bright blue
]

RESET = "\033[0m"

# === Get terminal width ===
width = shutil.get_terminal_size().columns

# === Split and print logo lines ===
lines = my_logo.strip("\n").splitlines()

for i, line in enumerate(lines):
    color = colors[i % len(colors)]          # Cycle through colors
    centered_line = line.center(width)       # Center according to terminal width
    print(f"{color}{centered_line}{RESET}")  # Print colored + centered line



def get_terminal_width() -> int:
    try:
        width, _ = get_terminal_size()
    except OSError:
        width = 80
    if system().lower() == "windows":
        width -= 1
    return width

#console.print("Get read to use....")

    

    
        
#console.print("Text check", style="bold green")


def main():
    clearScr()
    #display_menu()
def clearScr():
    if os.name == 'nt':  
        os.system('cls')
    else:  
        os.system('clear')