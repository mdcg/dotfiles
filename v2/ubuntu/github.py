from v2.ubuntu import (
    exec_update,
    exec_upgrade,
    exec_command,
)
from colorama import Fore, Style


def install_github(email):
    exec_update()
    exec_upgrade()

    exec_command(f'ssh-keygen -t ed25519 -C "{email}"')
    exec_command('eval "$(ssh-agent -s)"')
    exec_command(
        command="sudo apt-get install xclip",
        label=f"🪄 {Fore.GREEN}{Style.BRIGHT} Installing XClip...",
    )
    exec_command(
        command="xclip -selection clipboard < ~/.ssh/id_ed25519.pub",
        label=f"🪄 {Fore.GREEN}{Style.BRIGHT} SSH key was added to your clipboard. Add this value to your GitHub for the changes to take effect.",
    )
