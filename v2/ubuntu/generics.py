from v2.ubuntu import exec_command, exec_autoremove, exec_update, exec_upgrade, exec_full_upgrade

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
        exec_command(f"sudo apt-get install {util} -y")

    exec_update()
    exec_autoremove()