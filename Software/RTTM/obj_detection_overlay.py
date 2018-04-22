#
# obj_detection_overlay.py
#

import time
import numpy as np
import matplotlib.pyplot as plt

# 40"x30" inner dimensions
#
# |-------40"-------|
# 13.3"  13.3"  13.3"
# -------------------     ---
# |     |     |     | 15"  |
# |A    |B    |C    |      30"
# -------------------      |
# |     |     |     | 15"  |
# |D    |E    |F    |      |
#--------------------     ---
#
# Center points will be used for

t = np.arrange(0.0, 2.0, 0.01)
s = 1 + np.sin(2*np.pi*t)
plt.plot(t, s)

plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('Graph Practice')
plt.grid(True)
#plt.savefig("sin_wave.pgn")
plt.show()
