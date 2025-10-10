import os 
import subprocess 
import rich #type: ignore
dir_list=os.path.abspath("files/dir_list.txt")
sub_list=os.path.abspath ("files/sub_list")
admin_list= os.path.abspath("files/admin_list")
user_agent = "Mozilla/5.0s"
ffufrc = "~/.config/ffuf/ffufrc"
#ZSHRC Configuration Aliases 
alias r.firewall = 'uv run wafw00f' #type:ignore
alias r.zeal = 'uv run columns.py' #type:ignore
alias r.results = '' #type:ignore
#sub_list=os.path("~/lst/sub_list")