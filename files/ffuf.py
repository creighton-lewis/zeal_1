import os
import subprocess
import shutil
config = '~/.config/ffuf/ffufrc'
target = input("enter target:  ")
ffuf_file = f"{target}_ffuf"
os.system(f"ffuf -maxtime 20 -w wordlists/sub_list:SUB  -u https://SUB.{target} -t 100 -s -of md -o {ffuf_file} -mc 200-299,302,307 -H "'User-Agent: Mozilla/5.0'"")
def move_file():
    import shutil
    os.system(f"mv {ffuf_file} ..")
    os.chdir("..")
    shutil.copy("ffuf_file", "results/ffuf_file")
move_file()