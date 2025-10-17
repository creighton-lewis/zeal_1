import os
import shutil

def move_file(file_name: str | None = None) -> None:
    """
    Copy <file_name> from the current working directory to
    `../results/` (creating the target directory if needed).
    """
    if not file_name:
        file_name = input("Enter file name to move: ")

    src  = os.path.join(os.getcwd(), file_name)
    dst  = os.path.join("..", "results", file_name)

    # Ensure destination dir exists
    os.makedirs(os.path.dirname(dst), exist_ok=True)

    # Copy the file
    shutil.copy(src, dst)

    print(f"Copied {src} → {dst}")

# Do **not** run anything on import – let `poc.py` decide when to run.
# if __name__ == "__main__":
#     move_file()


"""import os
import shutil

def move_file(file_name = str):
    if file_name == None:
        file_name = input("Enter file name: ")
    current_path = os.getcwd() 
    print(current_path)
    file_path = os.path.join(current_path, file_name)
    destination = os.path.join("..", "results", file_name)
    os.makedirs(os.path.dirname(destination), exist_ok=True)
    shutil.copy(file_path, destination)
    print(f"Copied {file_path} to {destination}")
move_file()
"""