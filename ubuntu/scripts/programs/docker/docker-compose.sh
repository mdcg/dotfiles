#!/bin/bash

sudo apt-get update -y && sudo apt-get upgrade -y
sudo apt-get install docker-compose -y

# Reference: https://docs.docker.com/compose/install/
# You can also install this way:
# sudo curl -L "https://github.com/docker/compose/releases/download/1.29.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
# sudo chmod +x /usr/local/bin/docker-compose