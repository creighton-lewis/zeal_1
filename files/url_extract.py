import re
import os 
import sys
def url_extract(file: str | None = None):
  file = first_arg = sys.argv[1] if len(sys.argv) > 1 else None
  urlfile = f"{file}_urls"
  if not file:
    file = input("Enter file path:")
  os.system(f"cat {file}")
  os.system(f"grep 'https' {file} >> {urlfile}")
url_extract()