"""
Simple script to define your aliases.
Also your .bash_aliases or .zsh_aliases file must be exist,
If it isn't Alice will create it for you

So, put this lines into your shell rc

if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi

You can wrap this script in a function in your command shell rc file as sample:
alice() {
    python3 ~/path/to/Alice $@
    source ~/.zshrc
}
Alice in Wonderland care your aliases
"""

__version__ = "0.1.0"

import os
import re
import subprocess

from collections import OrderedDict
from math import ceil


class Alice:

    def __init__(self, home):
        # shell & aliases file path
        self.home = home
        self.config_path = f'{self.home}/.{str(os.environ["SHELL"][9:])}_aliases'

    def get_aliases(self):
        aliases = OrderedDict()
        mode = 'r' if os.path.exists(self.config_path) else 'a+'
        try:
            with open(self.config_path, mode) as f:
                for line in f.readlines():
                    clean = line.replace('"', '')
                    result = re.split(r'=', clean)
                    name = result[0].replace('alias', '').lstrip()
                    cmd = result[1].rstrip()
                    aliases[name] = cmd
            return aliases
        except Exception as e:
            raise e

    def source_aliases(self):
        try:
            cmd = f'source {self.home}/.{str(os.environ["SHELL"][9:])}rc'
            subprocess.call([os.environ["SHELL"],"-ic", cmd])
        except Exception as e:
            raise e

    def edit_aleases(self, editor):
        mode = 'a'
        initial_msg = False if os.path.exists(self.config_path) else True
        #  try popen process to editor
        try:
            with open(self.config_path, mode) as f:
                # if initial_msg:
                #     f.write('# Write your aliases here')
                subprocess.call([editor, self.config_path])
        except Exception as e:
            raise e

    @staticmethod
    def alias_paginate(ordered, page_counter: int):
        alias_menu_page_counter = page_counter
        pages = int(ceil(len(ordered) / 10))
        if alias_menu_page_counter <= pages:
            count = 0
            chunk = {}
            for key in ordered:
                if not count == 0:
                    if ((alias_menu_page_counter - 1) * 10) < count <= (alias_menu_page_counter * 10):
                        chunk[f"{count}. {key}"] = ordered[key]
                elif count == 0 and alias_menu_page_counter == 1:
                    chunk[f"{count}. {key}"] = ordered[key]
                count += 1

            return chunk
        else:
            return 0

