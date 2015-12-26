#!/usr/bin/env python
from __future__ import print_function

import os
from socket import gethostname
import datetime
import colorama

hostname=gethostname()
username = os.environ['USER']
pwd = os.getcwd()
homedir = os.environ['HOME']
pwd = pwd.replace(homedir, '~', 1)
# if len(pwd) > 30:
# pwd = pwd[:10]+'...'+pwd[-20:] # first 10 chars+last 20 chars
venv_name = os.getenv('VIRTUAL_ENV', "").split("/")[-1]
if venv_name:
	venv_name = "({venv_name})".format(venv_name=venv_name)

#"{virtualenv_name}{uname}@{host}:{path}\n[{time}]$ "

prompt = ""
#add virtualenv(if exists)


template = "\[{color}\]\[{style}\]{placeholder}\[{reset}\]"

prompt += template.format(color=colorama.Fore.MAGENTA, style=colorama.Style.BRIGHT, placeholder="{virtualenv_name}", reset=colorama.Style.RESET_ALL)

#add uname
prompt += template.format(color=colorama.Fore.GREEN, style=colorama.Style.BRIGHT, placeholder="{uname}", reset=colorama.Style.RESET_ALL)
prompt += template.format(color=colorama.Fore.CYAN, style=colorama.Style.BRIGHT, placeholder="@", reset=colorama.Style.RESET_ALL)

#add hostnam
prompt += template.format(color=colorama.Fore.YELLOW, style=colorama.Style.BRIGHT, placeholder="{host}", reset=colorama.Style.RESET_ALL)

prompt += template.format(color=colorama.Fore.CYAN, style=colorama.Style.BRIGHT, placeholder=":", reset=colorama.Style.RESET_ALL)
# prompt += colorama.Fore.CYAN + colorama.Style.BRIGHT + ":" + colorama.Style.RESET_ALL

#add path
prompt += template.format(color=colorama.Fore.BLUE, style="", placeholder="{path}", reset=colorama.Style.RESET_ALL)

# colorama.Fore.BLUE + "{path}" + colorama.Style.RESET_ALL
prompt += "\n"
#add time
prompt += template.format(color=colorama.Fore.RED, style="", placeholder="[{time}]", reset=colorama.Style.RESET_ALL)

# colorama.Fore.RED  + "[{time}]" + colorama.Style.RESET_ALL

#add prompt_end
prompt += template.format(color=colorama.Fore.CYAN, style=colorama.Style.BRIGHT, placeholder="$ ", reset=colorama.Style.RESET_ALL)
# colorama.Fore.CYAN + colorama.Style.BRIGHT + "$ " + colorama.Style.RESET_ALL



print(prompt.format(uname=username, host=hostname, path=pwd, virtualenv_name=venv_name, time=datetime.datetime.today().strftime('%H:%M:%S')))
