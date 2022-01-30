#!/bin/bash

sudo apt-get update -y && sudo apt-get upgrade -y
ssh-keygen -t ed25519 -C "<email>"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
sudo apt-get install xclip
xclip -selection clipboard < ~/.ssh/id_ed25519.pub