import os 
import requests #type:ignore
import subprocess #type:ignore
import rich #type:ignore
import nmap #type:ignore
import sys
from progressbar import ProgressBar #type:ignore
import shutil
from rich.console import Console #type:ignore
console = Console () #type:ignore

def clear_console():
    """Clears the console window."""
    os.system('cls' if os.name == 'nt' else 'clear')
#def display_banner():
  #  from banner import print_banner
  #  print(print_banner)
class Tech_Scan:
    def header(): 
        console.print(""" =======Tech Scan ======""", style = "bold cyan", justify="left")
    def get_input():
        target = console.input("\n Write target \n" )
        def tech_enum():
            os.system (f" uv run waf00f {target}")
            os.system(f"nmap -sV {target} --top-ports 40 -D RND:5 -Pn")
            os.system(f"nuclei -u {target}  -t nuclei-templates/dns")
            os.system(f"nuclei -u {target} -t nuclei-templates/http")
            os.system(f"nmap --script dns-brute-enum,http-sitemap-generator -sV {target} --top-ports 40 -D RND:5 -Pn")
        tech_enum()
    header() 
    get_input()

def main():
    try:
        Tech_Scan()
    except KeyboardInterrupt:
        print("Script interrupted by user.")

if __name__ == '__main__':
    main()
