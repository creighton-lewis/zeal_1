


import requests
import os 
import sys 

cve_list = [ 'CVE-2010-1000', 'CVE-2022-1010', 'CVE-2020-0001']
print (text)
from poc import Get_POC
poc = Get_POC()

for cve in cve_list:
    poc.get_poc(cve)
