import os #type: ignore
import subprocess
import requests #type: ignore
import rich #type: ignore
from rich.console import Console  #type:ignore
console = Console () #type:ignore
def clear_console():
        """Clears the console window."""
        os.system('cls' if os.name == 'nt' else 'clear')
clear_console()
console.print("VULN SCAN", style = "bold red", justify="left")
class Vuln_Scan():
    def vuln():
        from rich.console import Console #type: ignore
        console = Console ()
        target = console.input("\n Enter url or file \n")
        file_name = f"{target}_vuln"
        #target_file = os.path(input("Insert path"))
        os.system(f"sudo nmap -sV --script=vuln {target} -Pn -D RND:6 --scan-delay 10 -oX {file_name}")
        if os.path.exists(f"{file_name}"):
            try:
                os.system(f"uv run vulny.py -nm {file_name} --exploitdb --pstorm --nvd")
            except Exception as e:
                console.print(f"Error: {e}", style = "bold red")
    vuln()
        
def main():
    try:
        Vuln_Scan()
    except KeyboardInterrupt:
        print("Script interrupted by user.")

if __name__ == '__main__':
    main()
