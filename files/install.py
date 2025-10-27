import os 
import sys
def bin_scripts():
   if os.path.isdir('~/bin') == True:
    dst = '~/bin'
    loc = os.getcwd
def check_path():
    if os.path.exists("venv") == False:
        try:
            os.system(f"python3 -m venv venv")
            os.system(f"source venv/bin/activate")
        except:
           print("Unable to create virtual environment")
    elif os.path.exists("venv") == True:
        os.chdir("venv")
        os.system(f"git clone https://github.com/l4rm4nd/LinkedInDumper.git")
        os.system(f"mv LinkInDumper.git linkedin_info")
        os.system(f"git clone https://github.com/RUB-NDS/PRET.git")
        os.system(f"mv PRET.git pret_tool") 
        os.system(f"git clone https://raw.githubusercontent.com/praveenkavi5/PathSeeker/refs/heads/main/PathSeeker.py")
