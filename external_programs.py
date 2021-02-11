from subprocess import run, PIPE, CalledProcessError
from glob import glob
# from shlex import split
import shlex

cmd = "netstat -an"

try:
    proc = run(cmd)
except CalledProcessError as err:
    print(err)
    print(err.returncode)
else:
    print(proc.returncode)
    print("All is well.")
