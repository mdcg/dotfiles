from config.ubuntu import (
    exec_update,
    exec_upgrade,
    exec_command,
)
from colorama import Fore, Style


def install_ohmyzsh():
    exec_update()
    exec_upgrade()

    exec_command(
        command="sudo apt install zsh",
        label=f"🪄 {Fore.GREEN}{Style.BRIGHT} Installing ZSH...",
    )

    exec_command("chsh -s $(which zsh)")

    exec_command("chmod +x install.sh")
    exec_command(
        command="./install.sh",
        label=f"🪄 {Fore.GREEN}{Style.BRIGHT} Installing OhMyZsh...",
    )
