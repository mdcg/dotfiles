import signal
import sys

import click

from v2.ubuntu.brave import install_brave
from v2.ubuntu.docker import install_docker
from v2.ubuntu.generics import install_generic_utils
from v2.ubuntu.github import install_github
from v2.ubuntu.ohmyzsh import install_ohmyzsh
from v2.ubuntu.pyenv import install_pyenv
from v2.ubuntu.vscode import install_vscode


@click.group()
def cli():
    """This is a CLI to install MDCG's utils, libraries and dotfiles.

    \b
    You can contribute to improve this CLI by accessing:
    https://github.com/mdcg/dotfiles

    Enjoy! :)
    """
    pass


@cli.command()
@click.option(
    "--email", prompt="E-mail", help="Github e-mail to generate ssh key."
)
def full_install(email):
    install_generic_utils()
    install_ohmyzsh()
    install_pyenv()
    install_docker()
    install_vscode()
    install_brave()
    install_github(email)


def handle_sigterm(*args):
    raise SystemExit


if __name__ == "__main__":

    signal.signal(signal.SIGTERM, handle_sigterm)
    try:
        cli()
    except (KeyboardInterrupt, SystemExit):
        sys.exit(1)
