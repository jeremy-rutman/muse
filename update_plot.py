import numpy as np
import matplotlib.pyplot as plt

plt.axis([0, 10, 0, 1])
plt.ion()


xpos = 0
ypos = 0

while(1):

    y = (np.random.random()-0.5)/10.0
    x =( np.random.random()-0.5)/10.0
    xpos=xpos+x
    ypos=ypos+y
    plt.scatter(xpos, ypos)
    plt.pause(0.05)
    plt.ylim(ypos-1,ypos+1)
    plt.xlim(xpos-1,xpos+1)
while True:
    plt.pause(0.05)

