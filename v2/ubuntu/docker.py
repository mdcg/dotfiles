from v2.ubuntu import exec_update, exec_upgrade, exec_command
from colorama import Fore, Style

# #!/bin/bash

# # This installation will be done in two steps. The first we will install
# # all the dependencies necessary for the full functioning of Docker and
# # we will also add it to the "docker" group so that it is not necessary
# # to run the commands associated with it with "sudo".

# sudo apt-get update -y && sudo apt-get upgrade -y

# # Docker
# sudo apt-get remove -y docker docker-engine docker.io containerd runc
# sudo apt-get update -y
# sudo apt-get install -y apt-transport-https ca-certificates curl gnupg-agent software-properties-common
# curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
# sudo apt-key fingerprint 0EBFCD88
# sudo add-apt-repository \
#    "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
#    $(lsb_release -cs) \
#    stable"
# sudo apt-get update -y
# sudo apt-get install -y docker-ce docker-ce-cli containerd.io
# sudo groupadd docker
# sudo usermod -aG docker $USER
# newgrp docker

# echo "You need to log out and log back in so that your group membership be re-evaluated."
PREVIOUSLY_DOCKER_INSTALL_LIBRARIES = (
    "docker",
    "docker-engine",
    "docker.io",
    "containerd",
    "runc",
)

DOCKER_DEPENDENCIES = (
    "apt-transport-https",
    "ca-certificates",
    "curl",
    "gnupg-agent",
    "software-properties-common",
)


def install_docker():
    exec_update()
    exec_upgrade()

    for lib_to_del in PREVIOUSLY_DOCKER_INSTALL_LIBRARIES:
        exec_command(
            command=f"sudo apt-get remove {lib_to_del} -y",
            label=f"♻️ {Fore.RED}{Style.BRIGHT} Excluding {lib_to_del}...",
        )

    exec_update()

    for dep in DOCKER_DEPENDENCIES:
        exec_command(
            command=f"sudo apt-get install {dep} -y",
            label=f"🪄 {Fore.GREEN}{Style.BRIGHT} Installing {dep}...",
        )
