# Alice
Alice is console utilite which helps you manage and define your aliases easy.


Put this lines into your shell rc


bash

if [ -f ~/.zsh_aliases ]; then
    . ~/.zsh_aliases
fi


zsh

if [ -f ~/.zsh_aliases ]; then
    . ~/.zsh_aliases
fi

You can wrap this script in a function in your command shell rc file as sample:


bash example


alice() {
    python3 ~/path/to/Alice/main.py $@
    source ~/.bashrc
}

or for zsh

alice() {
    python3 ~/follow/the/white_rabbit/Alice/main.py $@
    source ~/.zshrc
}