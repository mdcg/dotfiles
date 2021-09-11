import signal
import sys

import click

from config.core import load_dependencies, load_dotfiles
from config.utils import handle_sigterm


@click.group()
def cli():
    """This is a CLI to install MDCG's utils, libraries and dotfiles.

    You can contribute to improve this CLI by accessing:
    https://github.com/mdcg/dotfiles

    Enjoy! :)
    """
    pass


@cli.command(short_help="Complete install of dependencies and dotfiles.")
@click.option("--email", prompt="E-mail", help="Github e-mail to generate ssh key.")
def full_install(email):
    """Installation of all essential MDCG utilities and libraries.

    It's a time-consuming installation that requires a lot of attention to the prompt.
    (it is possible that some permissions are required).
    """
    load_dependencies(email)
    load_dotfiles()


@cli.command(short_help="Installs dotfiles only.")
def install_dotfiles():
    """Dotfiles with aliases and other settings to help MDCG productivity and daily life.

    The skeletons of the files can be found in the "dotfiles" folder.
    """
    load_dotfiles()


if __name__ == "__main__":
    signal.signal(signal.SIGTERM, handle_sigterm)
    try:
        cli()
    except (KeyboardInterrupt, SystemExit):
        sys.exit(1)
