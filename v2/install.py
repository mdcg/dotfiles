import sys

from v2.ubuntu.docker import install_docker
from v2.ubuntu.generics import install_generic_utils
from v2.ubuntu.vscode import install_vscode
from v2.ubuntu.brave import install_brave
from v2.ubuntu.ohmyzsh import install_ohmyzsh
from v2.ubuntu.pyenv import install_pyenv
from v2.ubuntu.github import install_github


install_generic_utils()
install_ohmyzsh()
install_pyenv()
install_docker()
install_vscode()
install_brave()
install_github(sys.argv[1])
