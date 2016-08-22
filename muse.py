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

import numpy as np
import matplotlib.pyplot as plt

plt.axis([0, 1, 0, 1])
plt.ion()
plt.xlim(0, 1)
plt.ylim(0, 1)

plt.xlabel("mellow")
plt.ylabel("concentration")



proc = subprocess.Popen(["D:\\Program Files (x86)\\Muse\\muse-player.exe", "-l", "4999"], shell=True, stdout=subprocess.PIPE)

mellow = None
concentration = None

for line in iter(proc.stdout.readline, ''):
    if True:
        conc_match = re.search(r'/muse/elements/experimental/concentration f\s+([0-9.]+)', line)
        if conc_match:
            concentration = float(conc_match.group(1))

        mell_match = re.search(r'/muse/elements/experimental/mellow f\s+([0-9.]+)', line)
        if mell_match:
            mellow = float(mell_match.group(1))

        if mellow is not None and concentration is not None:
            print (mellow, concentration)
            plt.scatter(mellow, concentration)
            plt.pau se(0.05)
            mellow = None
            concentration = None

    if '/muse/elements/blink' in line and line.strip().endswith('1'):
        print line

    # if 'muse/elements/raw_fft' in line:
    #     match = re.search(r'([0-9. ]+)')
    #     if match:
    #         values = match.group(1).split(' ')
    #         print values
    #     else:
    #         print 1