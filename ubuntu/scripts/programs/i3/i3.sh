#!/bin/bash

sudo apt-get update -y && sudo apt-get upgrade -y
sudo apt-get install i3 i3blocks -y
i3-config-wizard
sed -i "$(( $(wc -l < ~/.config/i3/config)-2)),$ d" ~/.config/i3/config
cat bar >> ~/.config/i3/config