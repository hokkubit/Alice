import os

# User home dir
HOME = os.path.expanduser('~')

# You can define your prefered editor as Sublime, VS Code etc.
# by default is system editor

EDITOR = os.environ.get('EDITOR') if os.environ.get('EDITOR') else 'vim'
# EDITOR = 'subl'