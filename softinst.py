# script to install requested software

# import of the subprocess module

import subprocess

# creation of input variable

package_name = input('Which package do you want to install')
subprocess.run(["sudo", "apt", "install", "-y", package_name])

