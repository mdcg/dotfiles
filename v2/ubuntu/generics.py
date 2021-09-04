from v2.ubuntu import (
    exec_command,
    exec_autoremove,
    exec_update,
    exec_full_upgrade,
)
from colorama import Fore, Style


GENERICS_UTILS = (
    "make",
    "build-essential",
    "libssl-dev",
    "zlib1g-dev",
    "libbz2-dev",
    "libreadline-dev",
    "libsqlite3-dev",
    "wget",
    "curl",
    "llvm",
    "libncurses5-dev",
    "git",
    "tmux",
)


def install_generic_utils():
    exec_update()
    exec_full_upgrade()

    for util in GENERICS_UTILS:
        exec_command(
            command=f"sudo apt-get install {util} -y",
            label=f"🪄 {Fore.GREEN}{Style.BRIGHT} Installing {util}...",
        )

    exec_update()
    exec_autoremove()
