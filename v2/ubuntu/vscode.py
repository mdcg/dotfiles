from v2.ubuntu import exec_update, exec_command, install_packages
from colorama import Fore, Style

VSCODE_DEPENDENCIES = (
    "apt-transport-https",
    "wget",
)


def install_vscode():
    install_packages(VSCODE_DEPENDENCIES)

    exec_command(
        command="wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg",
        label=f"🛡️ {Fore.GREEN}{Style.BRIGHT} Downloading Microsoft VSCode GPG key...",
    )

    exec_command(
        "sudo install -o root -g root -m 644 packages.microsoft.gpg /etc/apt/trusted.gpg.d/"
    )
    exec_command(
        "sudo sh -c 'echo \"deb [arch=amd64,arm64,armhf signed-by=/etc/apt/trusted.gpg.d/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main\" > /etc/apt/sources.list.d/vscode.list'"
    )

    exec_command("rm -f packages.microsoft.gpg")

    exec_update()

    exec_command(
        command="sudo apt-get install code",
        label=f"🪄 {Fore.GREEN}{Style.BRIGHT} Installing VSCode...",
    )
