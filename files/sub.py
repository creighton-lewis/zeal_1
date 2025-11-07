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
        try:
            os.system(f"subfinder -d {target} -o {subdomains}") 
        except:
            console.print("unable to find or install subfinder")
        #os.system(f"assetfinder --subs-only {target} >> {subdomains}")
        def ffuf():
            console.print("Running ffuf....")
        try:
            os.system(f"ffuf -w wordlists/sub_list:SUB -u https://SUB.{target} -maxtime 1800 -t 100 -s -of md -o {ffuf_subs} -mc 200-299,302,307 -H "'User-Agent: Mozilla/5.0'" -or")
        except: 
             console.print("Unable to run ffuf, please try again ")
        def clean_subs():
            try:
                    console.print("Extracting urls......")
                    os.system(f"uv run ../url_extract.py -i {ffuf_subs} -s >> {subdomains}")
            except: 
                    console.print ("Unable to extract urls")
            try:
                    console.print("Checking which urls are active....")
                    os.system(f"~../url_active.sh {subdomains} ")

            except:
                    console.print("Unable to check which urls are active")
            console.print(f"Subdomains found in {subdomains} file.")
            from results import move_file
            try:
                move_file(subdomains)
                console.print(f"{subdomains} file successfully moved to results")
            except:
                console.print("Unable to move subdomains file")
            try:
                move_file(file_name1)
                console.print(f"{file_name1} file successfully moved to results")
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
