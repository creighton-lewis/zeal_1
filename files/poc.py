import requests
import os
from results import move_file          # ← the helper we’ll use

class GetPOC:
    """Very small CLI helper that downloads a CVE MD file and
    moves it to a `results/` directory."""
    
    def __init__(self):
        pass

    def get_poc(self, code: str | None = None) -> None:
        """
        Download the markdown file for *code* (e.g. "CVE‑2023‑1234") and
        hand it to `move_file()` so it ends up in `../results/`.
        """
        if code is None:
            code = input("Enter CVE code (e.g. CVE‑2023‑1234): ").strip()

        # Normalise the string so it *always* starts with "CVE-"
        if not code.upper().startswith("CVE-"):
            code = f"CVE-{code}"

        print(f"Fetching {code} …")

        # ----- 1️⃣  Pull the file -------------------------------------------------
        year = int(code.split("-")[1])                # e.g. 2023
        url  = f"https://raw.githubusercontent.com/trickest/cve/refs/heads/main/{year}/{code}.md"
        resp = requests.get(url)

        if resp.status_code == 404:
            print("❌  No references available")
            return
        print(resp)
        """ 
        # Store it locally first
        file_name = f"{code}.md"
        with open(file_name, "wb") as fh:
            fh.write(resp.content)

        # ----- 2️⃣  Move it to the results folder -------------------------------
        move_file(file_name)
        print(f"✅  Saved and moved {file_name}")
        """
def main() -> None:
    poc = GetPOC()
    poc.get_poc()            # runs the whole flow

if __name__ == "__main__":
    main()







"""import requests #type:ignore
import os
import sys
import re
#https://raw.githubusercontent.com/trickest/cve/refs/heads/main/2020/CVE-2020-11023.md
class Get_POC():
    #def __init__(self):
    #    pass
    def get_poc(code:str | None = None):
        if code is None:
            cve = code = input ("Enter code:")
        if 'CVE-' in code:
            year = int(code.split('-')[1])
            url = f"https://raw.githubusercontent.com/trickest/cve/refs/heads/main/{year}/{cve}.md"
            r = requests.get(url)
            status = r.status_code
            if status != 404:
             #   os.system(f"wget {url}")
            #if status != 400:
                os.system(f"wget {url}")
            else:
                print ("No references available")
        if 'CVE-' not in code:
            cve = f"CVE-{code}"
            print(cve)
            year = int(cve.split('-')[1])
            url = f"https://raw.githubusercontent.com/trickest/cve/refs/heads/main/{year}/{cve}.md"
            r = requests.get(url)
            status = r.status_code
            if status != 400:
                os.system(f"wget {url}")
            else:
                print("No references available")
        def open_file():
                try:
                    file_name = f"{cve}.md"
                    with open(file_name, 'r') as file:
                        pass
                except:
                    print("File was unable to download")
                def move_file():
                    from results import move_file
                    move_file(file_name)
                move_file()
        open_file()
    get_poc()
def main():
    try:
        Get_POC()
    except KeyboardInterrupt:
        print("Script interrupted by user.")
if __name__ == '__main__':
    main()
"""