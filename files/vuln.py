import os #type: ignore
import subprocess
import requests #type: ignore
import rich #type: ignore
from rich.console import Console  #type:ignore
console = Console () #type:ignore

def clear_console():
        """Clears the console window."""
        os.system('cls' if os.name == 'nt' else 'clear')

def read_urls_from_file(file_path):
    """Read URLs from a file, one URL per line."""
    try:
        with open(file_path, 'r') as f:
            return [line.strip() for line in f if line.strip()]
    except Exception as e:
        console.print(f"Error reading URL file: {e}", style="bold red")
        return []

clear_console()
console.print("VULN SCAN", style = "bold cyan")

class Vuln_Scan:
    def __init__(self):
        self.vuln()

    def scan_target(self, target):
        """Perform vulnerability scan on a single target."""
        file_name = f"{target}_vuln"
        file_name_2 = f"{target}_vuln_nikto"
        
        console.print(f"\nScanning target: {target}", style="bold yellow")
        #os.system(f"nikto -h {target} -no404 -Tuning 0,a,5,6,7,8,9,4 -Display 3 -evasion all -o {target}_nikto -Format csv")
        os.system(f"sudo nmap --script vuln,auth -sV {target} -Pn -D RND:6 --scan-delay 10 -oX {file_name}")
        
        if os.path.exists(f"{file_name}"):
            try:
                path = os.path.abspath(file_name)
                os.system(f"uv run exploitr/exploitr.py -nm {path} --all")
            except Exception as e:
                console.print(f"Error: {e}", style="bold red")
            try:
                os.system(f"uv run exploitr/exploitr.py -nm ../results/{file_name} --all")
            except:
                print("Unsucessful")
        from results import move_file 
        move_file(file_name)

    def vuln(self):
        console.print("\nChoose scan mode:", style="bold cyan")
        console.print("1. Single URL")
        console.print("2. Multiple URLs from file")
        
        choice = input("\nEnter your choice (1 or 2): ")
        
        if choice == "1":
            target = input("Enter URL: ")
            self.scan_target(target)
        elif choice == "2":
            file_path = input("Enter the path to your URL list file.Use the prefix ..results/file_name if located in the results directory: ")
            file_name = f"{file_path}_vulns"
            urls = read_urls_from_file(file_path)
            if urls:
                os.system(f"sudo nmap --script vuln,auth -sV -iL {file_path} -Pn -D RND:6 --scan-delay 10 -oX {file_name}")
            else:
                console.print("No valid URLs found in the file.", style="bold red")
        else:
            console.print("Invalid choice. Please run again and select 1 or 2.", style="bold red")

def main():
    try:
        clear_console()
        scanner = Vuln_Scan()
    except KeyboardInterrupt:
        print("Script interrupted by user.")

if __name__ == '__main__':
    main()
