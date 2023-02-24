import os
import locale

# User home dir
HOME = os.path.expanduser("~")

# By default is system editor. You can define your prefered editor as Sublime, VS Code, vim etc.
# EDITOR = "subl"
# EDITOR = "code"
EDITOR = os.environ.get("EDITOR") if os.environ.get("EDITOR") else "vim"

LANG = locale.getdefaultlocale()[0]

 
def get_shell_prefix():
    shell_pwd = os.environ["SHELL"][-4:]
    if (shell_pwd == 'bash'): 
        return shell_pwd
    else:
        return 'zsh'

def get_menu_lang(lang):
    return {
        'ru_RU': ('Редактировать alias комманды', 'Выполнить команду', 'Выход')
    }.get(lang, ('Edit alias list', 'Choose alias command', 'Exit'))



SHELL_PREFIX = get_shell_prefix()

MENU_LANG = get_menu_lang(LANG)