#! /usr/bin/env python3
import subprocess

# Create a script that runs a command with subprocess.run
# Check the exit status
# If exit status is good, run a second command.

oops = subprocess.check_call('ls -l', shell=True)
if oops:
	print("error")
else:
	print ("we did it!")
