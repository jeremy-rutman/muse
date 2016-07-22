# encoding: utf-8
'''
Connect the muse to the computer with BT.
use muse-io (in the command line) to read data from the muse thing.
with --osc 'osc.tcp://localhost:4999' because the default is port 5000 and
it won't work if there's another process on that port. port 4999 was fine.
read the data with muse-player. pass the port through '-l 4999'.
here I passed the output (which is verbose and not very well formatted) to a python subprocess
but I "hate" python 3 and some weird stuff happened. This sucks.
In summation:
1. Connect through BT
2. muse-io --osc 'osc.tcp://localhost:4999'
3. muse-player -l 4999 (in a different window because it's blocking obvs)
4. cry
'''
import subprocess
import re
import sys
# from matplotlib import pyplot as plt

# subprocess.call('dir', shell=True)
proc = subprocess.Popen(["D:\\Program Files (x86)\\Muse\\muse-player.exe", "-l", "4999"], shell=True, stdout=subprocess.PIPE)

for line in iter(proc.stdout.readline, ''):
	# print(line)
	if re.search('raw_fft[0-3]', line):
		print('hu')	
