#!/bin/bash

wget -L https://golang.org/dl/go1.16.4.linux-amd64.tar.gz
sudo rm -rf /usr/local/go && sudo tar -C /usr/local -xzf go1.16.4.linux-amd64.tar.gz
cat golang >> ~/.bashrc
rm go1.16.4.linux-amd64.tar.gz