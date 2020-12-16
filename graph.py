import numpy as np
import matplotlib.pyplot as plt
import time
import math
import time

start = time.time()

fig, ax = plt.subplots()
while True:
    # These should be the already-existing variables
    t = time.time() - start
    resonance = math.sin(t)/2 + .5
    pitch = math.cos(t)/2 + .5
    
    plt.cla()
    img = plt.imread("chart.png")
    plt.imshow(img)
    ax.imshow(img, extent=[0, 1, 0, 1])
    plt.scatter(pitch, resonance, s=200, color="#D32323")
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    
    
    plt.pause(5 / 1000)
    time.sleep(5/1000) # This will probably not be necessary with the time
                       # that already occurs between renders
plt.show()
