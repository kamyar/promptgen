### promptgen - python command prompt generator
====

#### USAGE
1. move either of the generator files to a permanent place(in this example as ".promptgen.py" at your home(~) directory)
    - **notice that in order to use colored prompt, you have to install colorama through pip:**
        - run `pip install colorama`
2. append following line to your .bashrc file located at your home directory:  
`export PROMPT_COMMAND='PS1="$(python ~/.promptgen.py)"'`
3. you are good to go!

#### Screenshots
![Alt text](/media/screenshot1.png?raw=true "Optional Title")

#### TODO
- Maybe have a config file to select what info(uname, current dir info, hostname, ip addr, etc.) the user wants to see and generate prompt accordingly?

#### CREDITS
This script was inspired by [this answer](http://askubuntu.com/a/17738/392647) on askubuntu.com

#### CONTRIBUTE
- Contributions and improvements are most welcome, just send the pull request. :)
