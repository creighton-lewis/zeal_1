import sys
import os 
import datetime
import requests #type:ignore
# Let user define the base url that they are interested  in 
def clear_console():
    """Clears the console window."""
    os.system('cls' if os.name == 'nt' else 'clear')
def inclusion():
    #response = input("Decide on using a folder or looping through a file")
    #if response == 1:
    target = input("Enter base url")
    company = target.split('.',1)[0]
    print(company)
    wordlist = "wordlists/injections"
    #with open ('wordlists/injections', 'r') as file:
     #    content = file.read()
    requests
    os.system(f"ffuf -u https://{target}/FUZZ -w {wordlist} -t 100 -v  -of md -mc 200,201,202,300,302 -o {company}")
    os.system(f"rm {company}")
inclusion()