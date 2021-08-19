import shlex
import subprocess
import sys

from yaspin import yaspin
from yaspin.spinners import Spinners

spinner = yaspin(Spinners.hamburger, color="green")


def process_stdout(proc):
    stdout = proc.stdout
    while stdout.readable():
        line = stdout.readline()
        if not line:
            break
        
        spinner.start()
        spinner.text = line.strip().decode("utf-8")

    check_for_errors(proc)
    spinner.text = "Done!"
    spinner.ok("✅ ")


def check_for_errors(proc):
    errors = proc.stderr.readlines()
    if errors:
        print_stderr(errors)
        sys.exit(1)


def print_stderr(errors):
    spinner.color = "red"
    for line in errors:
        spinner.text = line.strip().decode("utf-8")

    spinner.text = "Error!"
    spinner.fail("💥 ")


def exec_command(command):
    proc = subprocess.Popen(
        shlex.split(command),
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    process_stdout(proc)
    spinner.stop()
