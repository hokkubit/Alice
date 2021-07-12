import os


# User home dir
HOME = os.path.expanduser("~")

# By default is system editor. You can define your prefered editor as Sublime, VS Code etc.

EDITOR = os.environ.get("EDITOR") if os.environ.get("EDITOR") else "vim"
# EDITOR = "subl"
# EDITOR = "code"
