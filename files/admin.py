import os 
import subprocess
from rich.console import Console #type: ignore
console = Console ()
class Admin():
    def admin():
        console.print("FINDING ADMIN FILES...", style = "bold cyan" , justify = "left")
        WL = os.path.abspath("wordlists/admin_list")
        ffufrc = "~/.config/ffufrc/ffuf"
        file_name = console.input("Enter file name:")
        if os.path.exists(file_name) == True:
            console.print("File found")
            os.system(f"sed -i 'https://' {file_name}")
        with open() as f:
                for line in f:
                    os.system(f"ffuf -u https://{line} -w {WL} -config {ffufrc}")
        if os.path.exists(file_name) == False:
            console.print("Unable to find file,please retype path")
        
    admin()
