#!/bin/bash

sudo apt install zsh
chsh -s $(which zsh)
wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh
echo "Now run `sh install.sh`"
echo "If it can't works, reboot the machine."
