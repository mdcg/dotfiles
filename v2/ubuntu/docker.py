from v2.ubuntu import (
    exec_autoremove,
    exec_update,
    exec_upgrade,
    exec_command,
    install_packages,
)
from colorama import Fore, Style

DOCKER_LIBRARIES_TO_UNINSTALL = (
    "docker",
    "docker-engine",
    "docker.io",
    "containerd",
    "runc",
)


DOCKER_INSTALL_LIBRARIES = (
    "docker-ce",
    "docker-ce-cli",
    "containerd.io",
)

DOCKER_DEPENDENCIES = (
    "apt-transport-https",
    "ca-certificates",
    "curl",
    "gnupg",
    "gnupg-agent",
    "software-properties-common",
    "lsb-release",
)


def install_docker():
    exec_update()
    exec_upgrade()

    for lib_to_del in DOCKER_LIBRARIES_TO_UNINSTALL:
        exec_command(
            command=f"sudo apt-get remove {lib_to_del} -y",
            label=f"♻️ {Fore.RED}{Style.BRIGHT} Excluding {lib_to_del}...",
        )

    exec_autoremove()
    exec_update()

    install_packages(DOCKER_DEPENDENCIES)

    exec_command(
        "curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg"
    )
    exec_command(
        'echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null'
    )

    exec_update()

    install_packages(DOCKER_INSTALL_LIBRARIES)

    exec_update()
    exec_upgrade()

    exec_command(
        command="sudo systemctl enable docker",
        label=f"🪄 {Fore.GREEN}{Style.BRIGHT} Setting up Docker to start on boot...",
    )
    exec_command(
        command="docker run hello-world",
        label=f"🐋 {Fore.GREEN}{Style.BRIGHT} Testing Docker to check that everything is working correctly..",
    )
