# Packages required for gesture control

import sys
import subprocess
import pkg_resources

required = {'numpy','pandas','opencv-python','imutils','argparse'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed


if missing:
	# implement pip as a subprocess:
	subprocess.check_call([sys.executable, '-m', 'pip', 'install',*missing])


# process output with an API in the subprocess module:
reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

print("Installed Packages: ",installed_packages)