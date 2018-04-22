#CRUX:
#1. How to pull kinect sensor data
#2. How to throw away "useless" data, I.E. not the sandbox data
#3. Look up pyjector for python control of projector

#Nathan's Next Step:
#1. Pull data off sensor
#2. Restrict to sandbox
#3. Save off text file of sensor data of sandbox
#4. Plot sensor data
#5. Send to Randy

import matplotlib.pyplot as plt
from pykinect import nui
from pykinect2 import PyKinectV2
from pykinect2.PyKinectV2 import *



import os
import sys
import time
import numpy as np
#from pyjector import Pyjector

#Definitions for size of sandbox
length_of_sandbox = 0.3048 #Equates to 12"
width_of_sandbox = 0.3048 #Equates to 12"
heighth_threshold = 0.05 #Equates to 5cm

#Create vector of z-heights based on size of sandbox and threshold
#I.E.
# z = [z1, z2, z3, z4, z5, z6, z7, z8, z9, zn]

#Parse each vector of z-heights into sub-z-matricies
#I.E.
#z1 = [x1, y1, x2, y2, x3, y3, xn, yn]

#--------------------------------------------------------
#First Vectors to Plot

#This is for a single Z-height vector
#All x,y matrices

x1 = [10, 20, 25, 30, 40, 50, 60, 40, 50, 45, 40, 30, 23, 15, 8, 10, 10]
y1 = [10, 5, 15, 20, 15, 20, 30, 50, 60, 70, 80, 78, 70, 80, 60, 40, 10]

'''
x2 = []
y2 = []

x3 = []
y3 = []

x4 = []
y4 = []

x5 = []
y5 = []
'''
#First Plot
legend_name = ['z1', 'z2', 'z3', 'z4', 'z5']
plt.figure(1)
plt.plot(x1, y1, label = legend_name[0], linewidth = 2)
#plt.plot(x2, y2, label = legend_name[1], linewidth = 2)
#plt.plot(x3, y3, label = legend_name[2], linewidth = 2)
#plt.plot(x4, y4, label = legend_name[3], linewidth = 2)
#plt.plot(x5, y5, label = legend_name[4], linewidth = 2)

#plt.legend(loc = 'upper left')

plt.xlabel('X, 12" for Prototype')
plt.ylabel('Y, 12" for Prototype')
plt.title('Augmented Reality Sandbox')
#plt.grid(True)
plt.show(1)
#--------------------------------------------------------
def get_kinect_raw_data():
    #put shit here to grab raw sensor data
    #then return that this

# --------------------------------------------------------
def strip_kinect_raw_data():
    #take in the raw data and strip back to specified area
    #save off the data into a text file

# --------------------------------------------------------
def parse_kinect_data():
    #split off the data into the z-layer vectors/matrix

# --------------------------------------------------------