import os
import subprocess
import shutil
results_dir = "results"
config = '~/.config/ffuf/ffufrc'
target = input("enter target:  ")
os.system(f"touch {target}")
ffuf_file = target
#ffuf_file = f"{target}_ffuf"
#os.system(f"ffuf -maxtime 10 -w wordlists/sub_list:SUB  -u https://SUB.{target} -t 100 -s -of md -o {ffuf_file} -mc 200-299,302,307 -H "'User-Agent: Mozilla/5.0'"")
def move_file():
    import shutil
    os.system(f"mv {ffuf_file} ..")
    os.chdir("..")
    try:
            shutil.move(ffuf_file, os.path.join(results_dir, ffuf_file))
    except: 
            print("results not found, even though it exists")
move_file()