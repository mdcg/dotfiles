#!/bin/bash

sudo apt-get update -y && sudo apt-get upgrade -y
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev git
curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash
echo "Copying config to the ~/.bashrc and ~/.zshrc files"
cat config >> ~/.bashrc
cat config >> ~/.zshrc
echo "Run the command 'source ~/.bashrc <or> source ~/.zshrc' for the modifications to take effect."