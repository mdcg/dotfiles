#!/bin/bash

wget -L https://golang.org/dl/go1.17.6.linux-amd64.tar.gz
sudo rm -rf /usr/local/go && sudo tar -C /usr/local -xzf go1.17.6.linux-amd64.tar.gz
cat golang >> ~/.bashrc
cat golang >> ~/.zshrc
rm go1.17.6.linux-amd64.tar.gz
