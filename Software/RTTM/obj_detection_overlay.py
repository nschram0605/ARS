#
# obj_detection_overlay.py
#

import time
import numpy as np
import matplotlib.pyplot as plt
import scipy
import seaborn
import plotly.plotly as py
import plotly.tools as tls

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


mpl_fig = plt.figure()
ax = mpl_fig.add_subplot(111)
x = np.linspace(-10, 10, num=50)
y = np.sin(x)

line, = ax.plot(x, y, lw=1)

ax.set_title("Plot with Transparent Background")

plotly_fig =tls.mpl_to_plotly(mpl_fig)

plotly_fig = tls.mpl_to_plotly( mpl_fig )
plotly_fig["layout"].update({
                             "plot_bgcolor":"rgba(0, 0, 0, 0)",
                             "paper_bgcolor":"rgba(0,0,0,0)"
                             })

py.plot(plotly_fig)
'''
t = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
s = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
plt.plot(t, s)

plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('Graph Practice')
plt.grid(True)
plt.savefig("sin_wave.png", transparent=True)
plt.show()
'''