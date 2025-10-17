import os
import sys
import subprocess
from rich.console import Console #type: ignore 
console = Console ()
from rich import box #type: ignore 
from rich.table import Table #type: ignore 
from rich.progress import track #type: ignore 
#from files.banner import banner #type: ignore 
import shutil

if sys.version_info < (3, 0):
    print("This script requires Python 3.")
    sys.exit(1)
    
#from main import my_logo
#print(my_logo)
def main():
    from menus.main import my_logo
    #print(my_logo)
    #from test2 import my_logo_medium
    console = Console()
    #console.print(my_logo)
    #console.print(my_logo, style ="red")
    #console.print(print_logo, style ="red")
    #console.print(banner, style ="cyan")
    table = Table(box=box.ROUNDED)
    table.add_column("Information Gathering", justify="left", style="cyan bold", no_wrap=False, overflow="crop", ratio=1)
    table.add_column("Exploits", justify="left", style="red bold", no_wrap=False, overflow="crop", ratio=1)
    #table_values = 
    #table.add_column("Box Office", justify="left", style="green") 
    table.add_row("1. Directories", "8. CVE Search" , style= "bold")
    table.add_row("2. Subdomains", "9. See Results")
    table.add_row("3. Admin Paths", "10. Automated Exploit")
    table.add_row("4. Firewall Detection", "11.Brute Forcing")
    table.add_row("5. Vulnerability Check", "12.PRET Printer Exploit")
    table.add_row("6. Technology Check", "Rogue One: A Star Wars Story")
    table.add_row("7. Port Check ", "Rogue One: A Star Wars Story")
    #console.print("Text check", justify="left")
    #table.add_caption("Sample caption")
    console.print(table)
    selection = console.input("\nEnter input\n")
    if selection == "clear":
        subprocess.run("clear")
        subprocess.run(["uv" , "run" , "columns.py"])
    if selection == "1":
        os.chdir("files")
        subprocess.run(["uv" , "run", "dir.py"])
    elif selection == "2":
        import files.sub
    elif selection == "3":
        import files.admin
    elif selection == "4":
        console.print ("CHECKING FIREWALL", style = "bold cyan" , justify = "left")
        target = console.input ("Write url, or several urls separated by spaces")
        os.system(f"uv run wafw00f {target}")
        #from files.fire import firewall
    elif selection =="5":
        from files.vuln import vuln
    elif selection == "6": 
        from files import tech
    elif selection == "7": 
        console.print ("CHEKING OPEN PORTS", style = "bold cyan" , justify = "left")
        target = console.input ("Write url")
        os.system(f"rustscan -a {target}")
    elif selection == "8":
        import files.cve_report
    elif selection == "12":
        os.chdir("files")
        os.chdir("ext_programs")
        os.chdir("PRET")
        subprocess.run(["uv" , "run", "pret.py", "-h"])
        exit()
    elif selection == "9":
        exit()
#this HAS to be around
if __name__ == "__main__":
    main()
