import os 
import subprocess
import sys
import datetime
from rich.console import Console #type: ignore
console = Console ()
class Admin():
    def admin():
        ffufrc = "~/.config/ffufrc/ffuf"
        console.print("FINDING ADMIN FILES...", style = "bold cyan" , justify = "left")
        wl = "wordlists/adm_list"
        if wl == None:
            try:
                    subprocess.run(['uv', 'run' , 'wordlists/wordlist.py'])
                    os.chdir ("wordlists")
                    os.system("uv run wordlist.py")
                    os.system("cd ..")
                    wl = "wordlists/adm_list"
            except:
                    print("please add wordlist")
        print ("Choose between fuzzing a file or a list")
        console.print("Choose 1 for list")
        console.print("Choose 2 for url ")
        selection = input("Enter choice:")
        if selection == "clear":
                subprocess.run("clear")
                subprocess.run(["uv" , "run" , "admin.py"])
        if selection == "1":
                fir_dir = os.getcwd()
                print(fir_dir)
                subprocess.run(['cd' ,  '~/'])
                os.system(f"eza -l")
                file_name = console.input("Enter file with urls you want to find directories for")
                if os.path.join(file_name) == True:
                    console.print("File found")
                os.system(f"sed -i 'https://' {file_name}")
                with open() as f:
                        for line in f:
                            try:
                                os.system(f"ffuf -u https://{line}/FUZZ -w {wl} -config {ffufrc} -mc 200 -s")
                                os.system(f"ffuf -u https://{line}/FUZZ -w {wl} -mc 200 -s")
                            except:
                                print("Error")

        if selection == "2": 
              target = input("Provide target url")
              company = target.split('.',1)[0]
              print(company)
              file_name = f"{target}-admin-page"
              wl = "wordlists/adm_list"
              try: 
                os.system(f"ffuf -u https://{target}/FUZZ -w {wl} -t 100 -mc 200 -of md -o {file_name} -v -or")
              except:
                os.system (f"Unable to find admin directories my lord, please try again next time")
        if selection !="1" or "2":
             console.print("Please choose 1 or 2")
    admin()
Admin()

def main():
    try:
        Admin()
    except KeyboardInterrupt:
        print("Script interrupted by user.")

if __name__ == '__main__':
    main()
