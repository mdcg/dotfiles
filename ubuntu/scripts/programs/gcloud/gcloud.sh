#!/bin/bash

cd ~ && curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-336.0.0-linux-x86.tar.gz
tar xfvz google-cloud-sdk-336.0.0-linux-x86.tar.gz
./google-cloud-sdk/install.sh
echo "You need to start a new terminal for the changes to take effect."
echo "After the restart, run 'gcloud init' to start configuring the utility."