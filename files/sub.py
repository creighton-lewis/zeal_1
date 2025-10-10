import os 
import requests # type: ignore
import subprocess 
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
        target = console.input("\n Write target \n")
        sub_list = os.path.abspath("wordlists/sub_list")
        file_name = {target}.subs
        os.system(f"nmap -sV --script dns-brute,dns-service-discovery -sn -n {target} -oN {target}_dnsbrute")
        os.system(f"subfinder -d {target} -o {target}_subdomains")
        os.system(f"amass enum -d {target} -o {file_name}")
        os.system(f"assetfinder --subs-only {target} >> {target}_subdomains")
        os.system(f"ffuf -u https://FUZZ.{target} -t 100 -w {sub_list} -s -of md -o {file_name}")
        def extract_urls(file_name):
            from urlextract import URLExtract
            extractor = URLExtract()
            with open(f"{file_name}", 'r', encoding='utf-8') as file:
                text = file.read()
            urls = extractor.find_urls(text)
            output_file = f"{file_name}.urls"
            with open(output_file, 'w', encoding='utf-8') as f:
                for url in urls:
                    f.write(url + '\n')
            print(f"Extracted {len(urls)} URLs and saved to {output_file}")
        extract_urls()
    header()
    subdomain_enum()
    

def main():
    try:
        Sub_Find()
    except KeyboardInterrupt:
        print("Script interrupted by user.")

if __name__ == '__main__':
    main()
