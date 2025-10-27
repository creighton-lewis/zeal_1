import os 
import sys 

with open('wordlists/injections', 'r') as f: #open the file
    contents = f.readlines() #put the lines to a variable (list).
    print(contents)
