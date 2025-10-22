import os 
import sys 
import socket 
from rich.console import Console #type: ignore
#Create server
#Create password 
#Connect & ssh into server
#Define target 
#Determine open ports on target machine 
#Try to determine target machine type 
#Record in file 
#Start simple python server 
#Upload file 

console = Console () #type: ignore
def server_creation():
    from server import http_server
def ssh_connect():
    attack_val = sys.argv[1]
    if attack_val == None:
        attack_val = console.input("Enter ip address of the server you want to connect to")
    pass_val = sys.argv[2]
    if pass_val == None: 
        pass_val = console.input("Enter password")
def target_define():
    target_ip = console.input("Enter target ip ")
    if '.com' in target_ip or '.org' in target_ip or '.net' in target_ip:
        try:
            target_ip = socket.gethostbyname(target_ip)
            console.print(f"Resolved IP: {target_ip}", style="bold green")
        except socket.gaierror:
            console.print("Could not resolve hostname.", style="bold red")
            sys.exit(1)
    os.system(f"rustscan -a {target_ip}| tee -a open_ports")
    os.system(f"sed -i 's/{target_ip}//' open_ports") 
    # this should give a list of ports that look like this
    80 
    443 
    90
    20
    with open("open_ports", "r") as file: 
        content = file.read() 
        print(content) 
    for f in open_ports do: 
#Check what ports are open, prioritizing those under port 1,000
#Check if url 
#If url, provide ip address 
#Put
