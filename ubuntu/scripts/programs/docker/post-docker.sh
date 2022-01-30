#!/bin/bash

sudo apt-get update -y && sudo apt-get upgrade -y

# If you initially ran Docker CLI commands using sudo before adding your user
# to the docker group, you may see the following error, which indicates that
# your ~/.docker/ directory was created with incorrect permissions due to the
# sudo commands.

# WARNING: Error loading config file: /home/user/.docker/config.json -
# stat /home/user/.docker/config.json: permission denied

# To fix this problem, either remove the ~/.docker/ directory
# (it is recreated automatically, but any custom settings are lost),
# or change its ownership and permissions using the following commands:

# sudo chown "$USER":"$USER" /home/"$USER"/.docker -R
# sudo chmod g+rwx "$HOME/.docker" -R

# Configure Docker to start on boot:
sudo systemctl enable docker

# Testing to check that everything is working correctly.
docker run hello-world