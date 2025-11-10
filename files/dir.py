#Variable Import
import requests #type:ignore
import os 
import subprocess
import sys
import time
from rich.console import Console #type:ignore
console = Console () #type:ignore
from rich.table import Table #type:ignore
#from rich.progress import track
#init(autoreset=True)
def clear_console():
    """Clears the console window."""
    os.system('cls' if os.name == 'nt' else 'clear')

class Dir_Find:
    def dir_enum():
        console.print("FINDING Directory FILES...", style = "bold cyan" , justify = "left")
        target = console.input("Write target:")
        dir_list = "wordlists/dir_list"
        file_name = "{target}_directories"
    
        os.system(f"ffuf -u https://{target}/FUZZ -w {dir_list} -t 100 -of md -o {file_name} -p 0.10-0.30 -mc 200-299")
        os.system(f"../url_active.sh {file_name}")
        from results import move_file
        move_file(file_name)
    dir_enum()
def main():
    try:
        Dir_Find()
    except KeyboardInterrupt:
        print("Script interrupted by user.")

if __name__ == '__main__':
    main()
