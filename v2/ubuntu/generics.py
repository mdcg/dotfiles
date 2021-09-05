from v2.ubuntu import (
    exec_command,
    exec_autoremove,
    exec_update,
    exec_full_upgrade,
    install_packages,
)
from colorama import Fore, Style


GENERICS_DEPENDENCIES = (
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

    install_packages(GENERICS_DEPENDENCIES)

    exec_update()
    exec_autoremove()
