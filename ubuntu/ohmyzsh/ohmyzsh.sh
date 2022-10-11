#!/bin/bash

sudo apt install zsh
chsh -s $(which zsh)
sh -c "$(wget -O- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
echo "Now run `sh install.sh`"
echo "If it can't works, reboot the machine."
echo ">>> Remember: we like to use 'af-magic' theme <<<"
