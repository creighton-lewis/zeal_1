import json
import os 
from rich.console import Console #type:ignore
console = Console () #type:ignore
import subprocess
def to_results():  
    file_name = console.input ("\n Write file name \n") 
    old_place = os.path.abspath(file_name)
    print (old_place)    
    new_place = os.path.join(f"'Users', 'creightonlewis', 'Documents', 'Github', 'myenv' , 'kraken_copy', 'results', '{file_name}'")
    print (new_place)
    os.system(f"touch {new_place}")
    os.system(f"cat {old_place} >> {new_place}")
    os.path.exists(new_place)
to_results()
