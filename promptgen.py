#!/usr/bin/env python3

import os
from commands import getoutput
from socket import gethostname
import datetime
hostname = gethostname()
username = os.environ['USER']
pwd = os.getcwd()
homedir = os.path.expanduser('~')
pwd = pwd.replace(homedir, '~', 1)
# if len(pwd) > 30:
# pwd = pwd[:10]+'...'+pwd[-20:] # first 10 chars+last 20 chars
venv_name = os.getenv('VIRTUAL_ENV', "").split("/")[-1]
if venv_name:
	venv_name = "({venv_name})".format(venv_name=venv_name)
print("{virtualenv_name}{uname}@{host}:{path}\n[{time}]$ ".format(uname=username, host=hostname, path=pwd, virtualenv_name=venv_name, time=datetime.datetime.today().strftime('%H:%M:%S')))
