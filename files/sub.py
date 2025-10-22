import os 
import requests # type: ignore
import subprocess 
import shutil
import rich #type: ignore 
from rich.table import Table #type: ignore 
from colorama import Fore #type: ignore 
from rich.box import SIMPLE_HEAVY #type: ignore 
from rich.console import Console #type: ignore 
console = Console ()
def clear_console():
    """Clears the console window."""
    os.system('cls' if os.name == 'nt' else 'clear')

class Sub_Find:
    def subdomain_enum():
        console.print(f"""FINDING SUBDOMAINS...""", justify="left", style = "bold cyan")
        import subprocess
        target = console.input("Write target:")
        sub_list = "wordlists/sub_list"
        file_name1 = f"{target}_dnsbrute"
        subdomains = f"{target}_subdomains"
        ffuf_subs = f"{target}_ffuf"
        os.system(f"nmap -sV --script dns-brute,dns-service-discovery -sn -n {target} -oN {file_name1}")
        #os.system(f"subfinder -d {target} -o {subdomains}") 
        #os.system(f"assetfinder --subs-only {target} >> {subdomains}")
        os.system(f"ffuf -w wordlists/sub_list:SUB -u https://SUB.{target} -maxtime 20 -t 100 -s -of md -o {ffuf_subs} -mc 200-299,302,307 -H "'User-Agent: Mozilla/5.0'"")
        def clean_subs():
            try:
                    console.print("Extracting urls......")
                    os.system(f"~/bin/url_extract.sh {ffuf_subs} >> {subdomains}")
            except: 
                    console.print ("Unable to extract urls")
            try:
                    console.print("Checking which urls are active....")
                    os.system(f"chmod 700 url_active.sh")
                    os.system(f"./url_active.sh {subdomains}")
            except:
                    console.print("Unable to check which urls are active")
            console.print(f"Subdomains found in {subdomains} file.")
            from results import move_file
            try:
                move_file(subdomains)
            except:
                console.print("Unable to move subdomains file")
            try:
                move_file(file_name1)
            except:
                console.print("Unable to move {file_name1} file")
            try: 
                move_file(ffuf_subs)
            except:
                console.print("Unable to move {ffuf_subs} file")
        clean_subs()
    subdomain_enum()
    

def main():
    try:
        Sub_Find()
    except KeyboardInterrupt:
        print("Script interrupted by user.")

if __name__ == '__main__':
    main()
