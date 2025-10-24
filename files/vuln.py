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
console.print("VULN SCAN", style = "bold cyan")
class Vuln_Scan():
    def vuln():
        from rich.console import Console #type: ignore
        console = Console ()
        target = input("Enter url:" )
        file_name = f"{target}_vuln"
        file_name_2 = f"{target}_vuln_nikto"
        os.system(f"nikto -h {target} -no404 -Tuning 0,a,5,6,7,8,9,4 -Display 3 -evasion all -o {target}_nikto -Format csv")
        os.system(f"sudo nmap --script vuln,auth -sV {target} -Pn -D RND:6 --scan-delay 10 -oX {file_name}")
        if os.path.exists(f"{file_name}"):
            try:
                path = os.path.abspath(file_name)
                os.system(f"uv run exploitr/exploitr.py -nm {path} --all")
            except Exception as e:
                console.print(f"Error: {e}", style = "bold red")
        from results import move_file 
        move_file(file_name)
    vuln()
        
def main():
    try:
        clear_console()
        Vuln_Scan()
    except KeyboardInterrupt:
        print("Script interrupted by user.")

if __name__ == '__main__':
    main()
