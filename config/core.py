import os
import shutil
from pathlib import Path

from colorama import Fore, Style

from config.ubuntu.brave import install_brave
from config.ubuntu.docker import install_docker
from config.ubuntu.generics import install_generic_utils
from config.ubuntu.github import install_github
from config.ubuntu.ohmyzsh import install_ohmyzsh
from config.ubuntu.pyenv import install_pyenv
from config.ubuntu.vscode import install_vscode


def load_dotfiles():
    print(f"🪄 {Fore.GREEN}{Style.BRIGHT} Copying dotfiles...")
    CWD = Path().absolute()
    HOME = Path(os.environ["HOME"])
    shutil.copy(CWD / "config/dotfiles/.bashrc", HOME / ".bashrc")
    shutil.copy(CWD / "config/dotfiles/.aliases", HOME / ".aliases")
    print(f"✅ {Fore.GREEN}{Style.BRIGHT} Done!")


def load_dependencies(email):
    print(f"✨ {Fore.GREEN}{Style.BRIGHT} Starting full install!")
    install_generic_utils()
    install_ohmyzsh()
    install_pyenv()
    install_docker()
    install_vscode()
    install_brave()
    install_github(email)
    print("✅ {Fore.GREEN}{Style.BRIGHT} Done!")
