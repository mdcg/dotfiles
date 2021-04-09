# History control
HISTCONTROL=ignoreboth
HISTSIZE=1000
HISTFILESIZE=2000
shopt -s histappend

# Check the window size after each command and, if necessary,
# update the values of LINES and COLUMNS.
shopt -s checkwinsize

# Aliases
if [ -f ~/.aliases ]; then
    . ~/.aliases
fi

# Handlers
git_branch() {
	BRANCH=`git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/\1/'`
	if [ ! "${BRANCH}" == "" ]
	then
		echo " (${BRANCH}) "
	else
		echo " "
	fi
}

# Colors
export TERM=xterm-256color

TEXT_BLACK='\[\e[0;30m\]'
TEXT_RED='\[\e[0;31m\]'
TEXT_GREEN='\[\e[0;32m\]'
TEXT_YELLOWR='\[\e[0;93m\]'
TEXT_BLUE='\[\e[0;34m\]'
TEXT_PURPLE='\[\e[0;35m\]'
TEXT_CYAN='\[\e[0;96m\]'
TEXT_WHITE='\[\e[0;37m\]'

BOLD_BLACK='\[\e[1;30m\]'
BOLD_RED='\[\e[1;31m\]'
BOLD_GREEN='\[\e[1;32m\]'
BOLD_YELLOW='\[\e[1;33m\]'
BOLD_BLUE='\[\e[1;34m\]'
BOLD_PURPLE='\[\e[1;35m\]'
BOLD_CYAN='\[\e[1;36m\]'
BOLD_WHITE='\[\e[1;37m\]'

UNDERLINE_BLACK='\[\e[4;30m\]'
UNDERLINE_RED='\[\e[4;31m\]'
UNDERLINE_GREEN='\[\e[4;32m\]'
UNDERLINE_YELLOW='\[\e[4;33m\]'
UNDERLINE_BLUE='\[\e[4;34m\]'
UNDERLINE_PURPLE='\[\e[4;35m\]'
UNDERLINE_CYAN='\[\e[4;36m\]'
UNDERLINE_WHITE='\[\e[4;37m\]'

BACKGROUND_BLACK='\[\e[40m\]'
BACKGROUND_RED='\[\e[41m\]'
BACKGROUND_GREEN='\[\e[42m\]'
BACKGROUND_YELLOW='\[\e[43m\]'
BACKGROUND_BLUE='\[\e[44m\]'
BACKGROUND_PURPLE='\[\e[45m\]'
BACKGROUND_CYAN='\[\e[46m\]'
BACKGROUND_WHITE='\[\e[47m\]'

TEXT_RESET='\[\e[0m\]'

# Prompt colours
PROMPT_AT="${TEXT_CYAN}[\t]"
PROMPT_USERNAME="${TEXT_WHITE}\u"
PROMPT_HOST="${TEXT_WHITE}\h"
PROMPT_PATH="${TEXT_PURPLE}\w"
PROMPT_GIT_BRANCH="${BOLD_CYAN}\$(git_branch)"
PROMPT_UID="${TEXT_WHITE}>"
PROMPT_TEXT_RESET="${TEXT_RESET}"

# Red pointer for root
if [ "${UID}" -eq "0" ]; then
    PROMPT_UID="${TEXT_RED}>"
fi

export PS1="${PROMPT_PATH}${PROMPT_GIT_BRANCH}${PROMPT_UID}${PROMPT_TEXT_RESET} "

# Enable programmable completion features (you don't need to enable
# this, if it's already enabled in /etc/bash.bashrc and /etc/profile
# sources /etc/bash.bashrc).
if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi
