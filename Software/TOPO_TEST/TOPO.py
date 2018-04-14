# -------------------------------------------------------------------------------
# Title: TOPO.py
# Author: N. Schram
# Date: 2018-JAN-20
# Requirements: Anaconda Python, Python3
# Description:
# This script is the backend for projecting the retrieved data from
# the XBox Kinect V2 sensor.  This data was approximated from the TOPO_TEST.doc
# file that has the nested ellipses, simulating an actual topology.
# There are a total of 76 points taken from the test file.
# Data Format:
# (x, y, z)
# Topography color spectrum is ROYGBIV
# Where:
#           R is the tallest (Red)
#           V is the lowest (Violet)
# **Will still need to work out the bit values for such resolution
# For this example, there are ony 4 tiers: R, Y, B, V
# Colors can bg RGB or RBGA, lookup a color hex chart for explicit selection
#
# All dimensions are in inches
# -------------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import time
import csv

'''
# Scanned in Data from CSV File
# Uncomment to see the raw data in string format, will still need to be parsed
file = open('TOPO_TEST_Raw_Data_CSV.csv', 'r')
file1 =open
reader = csv.reader(file)
for row in reader:
    print(row)
'''

#ROYGBIV Hex Color Codes
R = '#FF0000'
O = '#FF7F00'
Y = '#FFFF00'
G = '#00FF00'
B = '#0000FF'
I = '#4B0082'
V = '#9400D3'

# Sandbox Dimensions (x, y, z) in inches:
sandbox_x_dim = 12
sandbox_y_dim = 12
sandbox_z_dim = 8


# Hard Coded Data
tier1_x = [0.25, 0.4, 0.8, 1.6, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11.6, 11.75, 11.6, 11.15, 10.2,
           9.7, 9, 8, 7, 6, 5, 4, 3, 1.8, 1, 0.45, 0.25]
tier1_y = [6, 7, 8, 9, 9.45, 10.2, 10.7, 11, 11.15, 11, 10.7, 10.25, 9.45, 8.4, 7,
           6, 5, 4, 3, 2.65, 2.2, 1.75, 1.5, 1.4, 1.5, 1.75, 2.25, 3, 4, 5, 6]
tier1_z = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
           1, 1, 1, 1, 1, 1, 1, 1]

tier2_x = [2.55, 2.85, 3.65, 5, 6, 7, 8, 9, 9.7, 10.55, 10.9, 10.75, 10, 9, 8, 7, 6, 5, 4, 3, 2.7, 2.55]
tier2_y = [6, 7, 8, 8.75, 9, 9.15, 8.85, 8.5, 8, 7, 6, 5, 4, 3.35, 2.9, 2.75, 2.8, 3.1, 3.6, 4.5, 5, 6]
tier2_z = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

tier3_x = [5.2, 5.7, 6.35, 7, 8, 9, 9.5, 10, 9.8, 9.55, 9, 8, 7, 6, 5.3, 5.2]
tier3_y = [6, 7, 7.55, 7.75, 7.75, 7.45, 7, 6.2, 5, 4.5, 4.2, 3.85, 3.9, 4.4, 5, 6]
tier3_z = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]

tier4_x = [7.8, 8, 8.5, 9, 9.4, 9.4, 9, 8.5, 8, 7.8, 7.8]
tier4_y = [6, 6.35, 6.6, 6.5, 6, 5.45, 5, 4.9, 5.2, 5.5, 6]
tier4_z = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]


# Legend Information
legend_name = ['Tier 1, Z=1"', 'Tier 2, Z=2"', 'Tier 3, Z=3"', 'Tier 4, Z=4"']

# Setting up axis tick interval: major and minor
ax = plt.axes()
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.25))
ay = plt.axes()
ay.yaxis.set_major_locator(ticker.MultipleLocator(1))
ay.yaxis.set_minor_locator(ticker.MultipleLocator(0.25))

# Plotting
# figsize creates a plot in inches
plt.figure(1, dpi=1000)
# plt.figure(1, figsize=(6, 6), dpi=1000)
# plt.figure(1, figsize=(sandbox_x_dim, sandbox_y_dim), dpi=100)  # Use this w/ projector
plt.plot(tier1_x, tier1_y, label=legend_name[0], linewidth=3, color=V)   # Tier 1, V
plt.plot(tier2_x, tier2_y, label=legend_name[1], linewidth=3, color=B)   # Tier 2, B
plt.plot(tier3_x, tier3_y, label=legend_name[2], linewidth=3, color=Y)   # Tier 3, Y
plt.plot(tier4_x, tier4_y, label=legend_name[3], linewidth=3, color=R)   # Tier 4, R
# plt.axis('equal')
plt.xlim(0, sandbox_x_dim)
plt.ylim(0, sandbox_y_dim)
plt.legend(loc='upper left')
plt.xlabel('X Axis - Length of Sandbox')
plt.ylabel('Y Axis - Height of Sandbox')
plt.title('Topographical Map of Augmented Reality Sandbox')
plt.grid(True)
plt.show()
