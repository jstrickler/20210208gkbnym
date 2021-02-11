from subprocess import run, PIPE, CalledProcessError
from glob import glob
# from shlex import split
import shlex

cmd = "netstat -an"

try:
    proc = run(cmd, stdout=PIPE)
    lines = proc.stdout.decode().splitlines()
    for line in lines:
        fields = line.split()
        if (len(fields) == 4) and (fields[-1] == 'ESTABLISHED'):
            local_addr, foreign_addr = fields[1:3]
            print(local_addr, foreign_addr)
except CalledProcessError as err:
    print(err)
    print(err.returncode)
else:
    print(proc.returncode)
    print("All is well.")
