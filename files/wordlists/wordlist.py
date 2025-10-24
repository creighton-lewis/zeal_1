import os
import subprocess
import sys 
if os.path.abspath("dir_list") == None: 
    os.system(f"curl -s https://raw.githubusercontent.com/xajkep/wordlists/refs/heads/master/discovery/directory_only_one.small.txt >> dir_list")
    os.system(f"curl -s https://raw.githubusercontent.com/3ndG4me/KaliLists/refs/heads/master/wfuzz/webservices/ws-dirs.txt >> dir_list")
    os.system(f"curl -s https://raw.githubusercontent.com/danielmiessler/SecLists/refs/heads/master/Fuzzing/LDAP.Fuzzing.txt >> dir_list")
    os.system(f"curl -s https://raw.githubusercontent.com/danielmiessler/SecLists/refs/heads/master/Discovery/Web-Content/api/api-endpoints.txt >> dir_list")
    os.system(f" sort -u dir_list -o dir_list")
if os.path.abspath("sub_list") == None:
    os.system(f"curl -s https://raw.githubusercontent.com/rajesh6927/subdomain-bruteforce-wordlist/refs/heads/main/Subdomain-wordlist.txt >> sub_list")
    os.system(f"curl -s https://raw.githubusercontent.com/n0kovo/n0kovo_subdomains/refs/heads/main/n0kovo_subdomains_large.txt >> sub_list")
    os.system(f"sort -u sub_list -o sub_list")
if os.path.abspath("usr_list") == None: 
    os.system(f"curl -s https://raw.githubusercontent.com/danielmiessler/SecLists/refs/heads/master/Usernames/sap-default-usernames.txt >> usr_list")
if os.path.abspath("adm_list"):
    os.system(f"curl -s https://raw.githubusercontent.com/the-robot/admin-finder/refs/heads/master/wordlist.txt >> adm_list")
if os.path.abspath("pass_list") == None: 
    os.system(f"curl -s https://raw.githubusercontent.com/berandal666/Passwords/refs/heads/master/10_million_password_list_top_1000000.txt >> pass_list")
if os.path.abspath("injections") == None: 
    os.system(f"curl -s https://raw.githubusercontent.com/1N3/IntruderPayloads/refs/heads/master/FuzzLists/vulnerability_discovery.txt >> injections")