from v2.ubuntu import (
    exec_update,
    exec_upgrade,
    exec_command,
    install_packages,
)
from colorama import Fore, Style

PYENV_DEPENDENCIES = (
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
)


def install_pyenv():
    exec_update()
    exec_upgrade()

    install_packages(PYENV_DEPENDENCIES)

    exec_command(
        command="curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash",
        label=f"🪄 {Fore.GREEN}{Style.BRIGHT} Installing Pyenv...",
    )

    pyenv_exports = '\n# Pyenv\nexport PYENV_ROOT=\\"\$HOME/.pyenv\\"\nexport PATH=\\"\$PYENV_ROOT/bin:\$PATH\\"\neval \\"\$(pyenv init --path)\\"\neval \\"\$(pyenv init -)\\"\neval \\"\$(pyenv virtualenv-init -)\\"\n'

    exec_command(
        command=f'echo "{pyenv_exports}" >> ~/.zshrc',
        label=f"🪄 {Fore.GREEN}{Style.BRIGHT} exporting pyenv to ~/.zshrc...",
    )
    exec_command(
        command=f'echo "{pyenv_exports}" >> ~/.bashrc',
        label=f"🪄 {Fore.GREEN}{Style.BRIGHT} exporting pyenv to ~/.bashrc...",
    )
