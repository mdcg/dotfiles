from v2.ubuntu import exec_update, exec_command, install_packages
from colorama import Fore, Style


BRAVE_DEPENDENCIES = (
    "apt-transport-https",
    "curl",
)


def install_brave():
    install_packages(BRAVE_DEPENDENCIES)
    exec_command(
        command="sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg",
        label=f"🛡️ {Fore.GREEN}{Style.BRIGHT} Downloading Brave GPG key...",
    )

    exec_command(
        'echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg arch=amd64] https://brave-browser-apt-release.s3.brave.com/ stable main"|sudo tee /etc/apt/sources.list.d/brave-browser-release.list'
    )

    exec_update()

    exec_command(
        command="sudo apt install brave-browser",
        label=f"🪄 {Fore.GREEN}{Style.BRIGHT} Installing Brave...",
    )
