import os 
import sys
import subprocess
cwd = os.getcwd()
os.system(f"cd ~/")
os.system(f"eza -T")
#os.system(f"cd {cwd}")
file_name = input("Enter file path:")
file_path = os.path.abspath(f"{file_name}")
print(file_name)

#f = open (f'{file_name}', 'r')
#for line in f:
#    url = line.strip()
#    os.system(f"uv run fuxploider/fuxploider.py -u line  --not-regex regex --random-user-agent")
#f.close()