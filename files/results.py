import os
import shutil

file_name = input("Enter file name: ")
current_path = os.getcwd() 
print(current_path)

file_path = os.path.join(current_path, file_name)
destination = os.path.join("..", "results", file_name)

os.makedirs(os.path.dirname(destination), exist_ok=True)
shutil.copy(file_path, destination)

print(f"Copied {file_path} to {destination}")
