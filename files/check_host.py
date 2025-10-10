#!/usr/bin/env python3
import sys
import subprocess
import os

file = sys.argv[1]
temp_file = f"{file}.tmp"

with open(file, 'r') as f_in, open(temp_file, 'w') as f_out:
    for ip in f_in:
        ip = ip.strip()
        result = subprocess.run(
            ["nmap", "-sn", ip],
            capture_output=True,
            text=True
        )
        
        if "Host is up" in result.stdout:
            print(f"Ping successful, host active: {ip}")
            f_out.write(f"{ip}\n")
        else:
            print(f"Ping unsuccessful: {ip}")

# Replace original file with filtered results
os.replace(temp_file, file)
print(f"\n[+] File updated: {file}")
