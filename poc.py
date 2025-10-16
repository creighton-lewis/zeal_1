import requests
import os
import sys
import re
#https://raw.githubusercontent.com/trickest/cve/refs/heads/main/2020/CVE-2020-11023.md
class Get_POC():
    def get_poc(self,code=None):
        cve = code = input ("Enter code:")
        if 'CVE-' in code:
            year = int(code.split('-')[1])
            url = f"https://raw.githubusercontent.com/trickest/cve/refs/heads/main/{year}/{cve}.md"
            r = requests.get(url)
            status = r.status_code
            if status != 400:
                os.system(f"wget {url}")
        if 'CVE-' not in code:
            cve = f"CVE-{code}"
            print(cve)
            year = int(cve.split('-')[1])
            url = f"https://raw.githubusercontent.com/trickest/cve/refs/heads/main/{year}/{cve}.md"
            r = requests.get(url)
            status = r.status_code
            if status != 400:
                os.system(f"wget {url}")
            def open_file():
                try:
                    file_name = f"{cve}.md"
                    with open(file_name, 'r') as file:
                        pass
                except:
                    print("File was unable to download")
            open_file()
    get_poc()
def main():
    try:
        Get_POC()
    except KeyboardInterrupt:
        print("Script interrupted by user.")
if __name__ == '__main__':
    main()
