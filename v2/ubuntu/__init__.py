from os import system

from colorama import init, Fore, Style

init(autoreset=True)


def exec_command(command, label=None):
    if label:
        print(label)
    system(command)


def exec_update():
    exec_command(
        command="sudo apt-get update -y",
        label=f"🚀 {Fore.WHITE}{Style.BRIGHT} Updating system...",
    )


def exec_upgrade():
    exec_command(
        command="sudo apt-get upgrade -y",
        label=f"⚙️ {Fore.WHITE}{Style.BRIGHT} Upgrading system...",
    )


def exec_full_upgrade():
    exec_command(
        command="sudo apt full-upgrade -y",
        label=f"🔧⚙️ {Fore.WHITE}{Style.BRIGHT} Full updating system...",
    )


def exec_autoremove():
    exec_command(
        command="sudo apt autoremove -y",
        label=f"♻️ {Fore.RED}{Style.BRIGHT} Removing unnecessary libraries...",
    )
