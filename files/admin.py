import os 
import subprocess
import sys
from rich.console import Console #type: ignore
console = Console ()
class Admin():
    def admin():
        console.print("FINDING ADMIN FILES...", style = "bold cyan" , justify = "left")
        WL = os.path.abspath("wordlists/admin_list")
        if WL == None: 
             os.system(f"uv run wordlists/wordlist.py")
        ffufrc = "~/.config/ffufrc/ffuf"
        print ("Choose between fuzzing a file or a list")
        selection = input("Make selection, file for 1 and a link for two")
        if selection == "clear":
                subprocess.run("clear")
                subprocess.run(["uv" , "run" , "columns.py"])
        if selection == 1:
                (f"cd ~/ ")
                (f"os.system cd ~/ ")
                file_name = console.input("Enter file name:")
                if os.path.exists(file_name) == True:
                    console.print("File found")
                os.system(f"sed -i 'https://' {file_name}")
                with open() as f:
                        for line in f:
                            os.system(f"ffuf -u https://{line} -w {WL} -config {ffufrc}")
        if selection == 2:
            try: 
              os.system(f"cd ~/")
              os.system(f"eza -l")
              
            except: 
                os.system (f"Unable to find admin directories my lord, please try again next time")
    admin()
Admin()

def main():
    try:
        Admin()
    except KeyboardInterrupt:
        print("Script interrupted by user.")

if __name__ == '__main__':
    main()
