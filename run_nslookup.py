from subprocess import run, PIPE, CalledProcessError

site = 'www.google.com'

cmd = ['nslookup']

cmd.append(site)

try:
    proc = run(cmd, stdout=PIPE)
    if proc.returncode == 0:
        addresses = []
        raw_output = proc.stdout.decode()
        lines = raw_output.splitlines()
        for line in lines:
            if line.startswith('Address:'):
                _, addr = line.split()
                addresses.append(addr)
    addresses.pop(0)  # remove first address
    print(addresses)
except CalledProcessError as err:
    print(err)

