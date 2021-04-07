#!/bin/bash

sudo apt-get update -y && sudo apt-get upgrade -y
sudo apt-get install i3 i3blocks -y
i3-config-wizard

# https://www.baeldung.com/linux/remove-last-n-lines-of-file
sed -i "$(( $(wc -l < ~/.config/i3/config)-3+1)),$ d" ~/.config/i3/config

cat bar >> ~/.config/i3/config
exit 0