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

__version__ = "0.1.1"
