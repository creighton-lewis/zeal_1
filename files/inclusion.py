import sys
import os 
import requests 
# Let user define the base url that they are interested  in 
base_url = input("Enter base url")
def inclusion():
    os.path.abspath("wordlists/file_upload")
    os.system(f"ffuf -u https://{base_url}FUZZ -w wordlist/file_upload")