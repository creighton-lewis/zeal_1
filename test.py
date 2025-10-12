
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

def tables():
        from main import my_logo
        console = Console()
        table = Table(box=box.SIMPLE, expand = True)
        table.add_column("Information Gathering", justify="left", style="cyan bold", no_wrap=False, overflow="crop", ratio=1)
            #table_values = 
            #table.add_column("Box Office", justify="left", style="green") 
        table.add_row("1. Directories")
        table.add_row("2. Subdomains")
        table.add_row("3. Admin Path")
        table.add_row("4. Vuln Check") 
        table.add_row("5. Technology Check")
        table.add_row("6. Port Check")
        table.add_row("7. AI Analysis")
        table.add_row("8. Network Analysis")
        table.add_row("9. Check Host Status")
        table.add_row("10. Start Server")
        table.add_row("11. Broken Links")
        table.add_row("12. Check File Upload Vulnerability")
        console.print(table)
        table = Table(box=box.SIMPLE, expand = True)
        table.add_column("Exploiting", justify="left", style="cyan bold", no_wrap=False, overflow="crop", ratio=1)
        table.add_row("A. Directories")
        table.add_row("B. Subdomains")
        table.add_row("C. Subdomains")
        console.print(table)
        selection = console.input("\nEnter input\n")
        if selection == "clear":
                subprocess.run("clear")
                subprocess.run(["uv" , "run" , "columns.py"])
        if selection == "1":
                import files.dir
        elif selection == "2":
                import files.sub
        elif selection == "3":
                import files.admin
        elif selection =="4":
                import files.vuln
        elif selection == "5": 
                import files.tech
    
    #this HAS to be around

def main():
    try:
        tables()
    except KeyboardInterrupt:
        print("Script interrupted by user.")

if __name__ == '__main__':
    main()
