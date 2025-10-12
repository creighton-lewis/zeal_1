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
    def header():
        console.print(f"""FINDING SUBDOMAINS...""", justify="left", style = "bold green")
    def subdomain_enum():
        import subprocess
        target = console.input("\n Write target \n")
        sub_list = "wordlists/sub_list"
        file_name1 = f"{target}_dnsbrute"
        subdomains = f"{target}_subdomains"
        ffuf_subs = f"{target}_ffuf"
        os.system(f"nmap -sV --script dns-brute,dns-service-discovery -sn -n {target} -oN {file_name1}")
        if subprocess.run(["subfinder"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL):
            print("Command exists and is executable.")
            os.system(f"subfinder -d {target} -o {subdomains}")
            print("Command does not exist in the PATH.")   
        if subprocess.run(["subfinder"], check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL):
             console.print("Skipping subfinder ")
        if subprocess.run(["assetfinder --subs-only {target}",check=True,stdout.subrpocess.DEVNULL,st
        os.system(f"assetfinder --subs-only {target} >> {subdomains}")
        if os.path.exists("~/.config/ffuf/ffufrc"):
            config = "~/.config/ffuf/ffufrc"
            os.system(f"ffuf -u https://FUZZ.{target} -t 100 -w {sub_list} -s -of md -o {ffuf_subs} -config {config}")
        elif os.path.exists == "False":
            os.system(f"ffuf -u https://FUZZ.{target} -t 100 -w {sub_list} -s -of md -o {ffuf_subs}")
        console.print("Unable to run Ffuf")
        try:
                os.system(f"bin/url.sh{ffuf_subs} >> {subdomains}")
                os.system(f"~/bin/url_extract.sh{ffuf_subs} >> {subdomains}")
        except:
                console.print("Unable to find files")
        os.system(f"rm {ffuf_subs}")
        console.print(f"Subdomains found in {subdomains} file.")
        if os.path.exists(file_name1):   
            os.system(f"mv {file_name1} ..")
        os.system(f"mv {subdomains} ..")
        os.chdir("..")
        shutil.move("file_name1", "results/file_name1")
        shutil.move("subdomains", "results/subdomains")
    header()
    subdomain_enum()
    

def main():
    try:
        Sub_Find()
    except KeyboardInterrupt:
        print("Script interrupted by user.")

if __name__ == '__main__':
    main()
