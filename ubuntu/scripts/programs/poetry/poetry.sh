#!/bin/bash

curl -sSL https://install.python-poetry.org | python3 -
cat config >> ~/.bashrc
cat config >> ~/.zshrc

