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
        console.print("""FINDING DIRECTORIES...""", justify = "left", style = "bold green")
        target = console.input("\n Write target \n")
        dir_list = os.path.abspath("wordlists/dir_list.txt")
        file_name = f"{target}_directories"
        #target = console.input("\n Write target \n")
        os.system(f"ffuf -u https://{target}/FUZZ -w {dir_list} -t 100 -s -of md -o {file_name} -p 0.10-0.3")
        def extract_urls():
            from urlextract import URLExtract
            extractor = URLExtract()
            with open('filename', 'r') as file:
                text = file.read()
                urls = extractor.find_urls(text)
                print(urls)
        extract_urls(file_name)
    dir_enum()

def main():
    try:
        Dir_Find()
    except KeyboardInterrupt:
        print("Script interrupted by user.")

if __name__ == '__main__':
    main()
