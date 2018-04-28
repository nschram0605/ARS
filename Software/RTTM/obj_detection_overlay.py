###########################################################################################
###
### program: obj_detection_overlay.py
###
### author: n.schram
###
### date: 2018-APRL-21
###
### description: the purpose of this program is to plot a circle in red of diameter 15".
### the function will take the x, y location information for the center of the circle.
###
###########################################################################################

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
# -------------------     ---

# |----------- 40" -------|
# |-10"-|
# ------------------------- -------
# |  1  |  2  |  3  |  4  |  10" |
# |  A  |  B  |  C  |  D  |   |  |
# ------------------------- ---- |
# |  5  |  6  |  7  |  8  |      |
# |  E  |  F  |  G  |  H  |     30"
# -------------------------      |
# |  9  | 10  | 11  | 12  |      |
# |  I  |  J  |  K  |  L  |      |
# -------------------------     ---

# Projector outputs the image size in pixels: 1024x768

import time
import numpy as np
import matplotlib.pyplot as plt
#from matplotlib.ticker import MultipleLocator, FormatStrFormatter

import scipy
import seaborn

# Position of circle, this comes from the detector circuit
# Object detection location: will change the location variable (A-F)
location = 'A'
location_list = ['A', 'B', 'C', 'D', 'E', 'F', 'AB', 'BC', 'DE', 'EF', 'AD', 'BE', 'CF', 'ABDF', 'BCEF']

# Detector circle dimensions in inches
circle_r = 7.5
circle_d = 15
circle_r_pixels = 192
circle_d_pixels = 384

# global sandbox size in inches & pixels
global_x = 40
global_y = 30
global_x_pixels = 1024
global_y_pixels = 768

# Define all position variables for circles in inches
# Total of 15 Detection Zones

a_circle = [7.5, 22.5]
b_circle = [20, 22.5]
c_circle = [32.5, 22.5]
d_circle = [7.5, 7.5]
e_circle = [20, 7.5]
f_circle = [32.5, 7.5]

ab_circle = [13.3, 22.5]
bc_circle = [26.6, 22.5]
de_circle = [13.3, 7.5]
ef_circle = [26.6, 7.5]
ad_circle = [7.5, 15]
be_circle = [20, 15]
cf_circle = [32.5, 15]

abdf_circle = [13.3, 15]
bcef_circle = [26.6, 15]

# circle_r_pixels = 192

# pixel equivalent of 20: 512
# pixel equivalent of 22.5: 576
# pixel equivalent of 32.5: 832

a_circle_pixels = [192, 576]
b_circle_pixels = [512, 576]
c_circle_pixels = [832, 576]
d_circle_pixels = [192, 192]
e_circle_pixels = [512, 192]
f_circle_pixels = [832, 192]

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# BEGINNING OF FUNCTION DEFINITIONS.

# -------------------------------------------------------->
def get_centerpoint_location_for_plotting(location):


    local_label = 'N/A'
    #x_val = 'N/A';
    #y_val = 'N/A';

    if (location == 'A'):
        print('Location: ', location)
        location_label = 'A'
        x_val = a_circle[0]
        y_val = a_circle[1]
        print('---> x_val: ', x_val, " y_val: ", y_val)
    elif (location == 'B'):
        print('Location: ', location)
        location_label = 'B'
        x_val = b_circle[0]
        y_val = b_circle[1]
        print('---> x_val: ', x_val, " y_val: ", y_val)
    elif (location == 'C'):
        print('Location: ', location)
        location_label = 'C'
        x_val = c_circle[0]
        y_val = c_circle[1]
        print('---> x_val: ', x_val, " y_val: ", y_val)
    elif (location == 'D'):
        print('Location: ', location)
        location_label = 'D'
        x_val = d_circle[0]
        y_val = d_circle[1]
        print('---> x_val: ', x_val, " y_val: ", y_val)
    elif (location == 'E'):
        print('Location: ', location)
        location_label = 'E'
        x_val = e_circle[0]
        y_val = e_circle[1]
        print('---> x_val: ', x_val, " y_val: ", y_val)
    elif (location == 'F'):
        print('Location: ', location)
        location_label = 'F'
        x_val = f_circle[0]
        y_val = f_circle[1]
        print('---> x_val: ', x_val, " y_val: ", y_val)
    elif (location == 'AB'):
        print('Location: ', location)
        location_label = 'AB'
        x_val = ab_circle[0]
        y_val = ab_circle[1]
        print('---> x_val: ', x_val, " y_val: ", y_val)
    elif (location == 'BC'):
        print('Location: ', location)
        location_label = 'BC'
        x_val = bc_circle[0]
        y_val = bc_circle[1]
        print('---> x_val: ', x_val, " y_val: ", y_val)
    elif (location == 'DE'):
        print('Location: ', location)
        location_label = 'DE'
        x_val = de_circle[0]
        y_val = de_circle[1]
        print('---> x_val: ', x_val, " y_val: ", y_val)
    elif (location == 'EF'):
        print('Location: ', location)
        location_label = 'EF'
        x_val = ef_circle[0]
        y_val = ef_circle[1]
        print('---> x_val: ', x_val, " y_val: ", y_val)
    elif (location == 'AD'):
        print('Location: ', location)
        location_label = 'AD'
        x_val = ad_circle[0]
        y_val = ad_circle[1]
        print('---> x_val: ', x_val, " y_val: ", y_val)
    elif (location == 'BE'):
        print('Location: ', location)
        location_label = 'BE'
        x_val = be_circle[0]
        y_val = be_circle[1]
        print('---> x_val: ', x_val, " y_val: ", y_val)
    elif (location == 'CF'):
        print('Location: ', location)
        location_label = 'CF'
        x_val = cf_circle[0]
        y_val = cf_circle[1]
        print('---> x_val: ', x_val, " y_val: ", y_val)
    elif (location == 'ABDF'):
        print('Location: ', location)
        location_label = 'ABDF'
        x_val = abdf_circle[0]
        y_val = abdf_circle[1]
        print('---> x_val: ', x_val, " y_val: ", y_val)
    elif (location == 'BCEF'):
        print('Location: ', location)
        location_label = 'BCEF'
        x_val = bcef_circle[0]
        y_val = bcef_circle[1]
        print('---> x_val: ', x_val, " y_val: ", y_val)

    # HAND-OFF TO FUNCTION
    display_circle_stepthrough(x_val, y_val, circle_r, location_label)

# <--------------------------------------------------------

# --------------------------------------------------------->
def display_circle_stepthrough(x, y, circle_radius, label_location):

    fig = plt.figure()

    ax = fig.add_subplot(1, 1, 1)

    ax.axis('scaled')

    major_ticks_x = np.arange(0, global_x + 1, 5)
    minor_ticks_x = np.arange(0, global_x + 1, 1)
    major_ticks_y = np.arange(0, global_y + 1, 5)
    minor_ticks_y = np.arange(0, global_y + 1, 1)

    ax.set_xticks(major_ticks_x)
    ax.set_xticks(minor_ticks_x, minor=True)
    ax.set_yticks(major_ticks_y)
    ax.set_yticks(minor_ticks_y, minor=True)

    ax.grid(which='both')
    ax.grid(which='minor', alpha=0.2)
    ax.grid(which='major', alpha=0.5)

    #plt.title('Location: ', label_location)

    circle = plt.Circle((x, y), linewidth=5, radius=circle_radius, color='red', fill=False)
    plt.gcf().gca().add_artist(circle)

    plt.show()
# <--------------------------------------------------------

# --------------------------------------------------------->
def display_circle_cont(x, y, circle_radius, label_location):

    plt.ion()

    fig = plt.figure()

    # ax = fig.add_subplot(1, 1, 1)
    ax = fig.add_subplot(111)

    ax.axis('scaled')

    major_ticks_x = np.arange(0, global_x + 1, 5)
    minor_ticks_x = np.arange(0, global_x + 1, 1)
    major_ticks_y = np.arange(0, global_y + 1, 5)
    minor_ticks_y = np.arange(0, global_y + 1, 1)

    ax.set_xticks(major_ticks_x)
    ax.set_xticks(minor_ticks_x, minor=True)
    ax.set_yticks(major_ticks_y)
    ax.set_yticks(minor_ticks_y, minor=True)

    ax.grid(which='both')
    ax.grid(which='minor', alpha=0.2)
    ax.grid(which='major', alpha=0.5)

    circle = plt.Circle((x, y), linewidth=5, radius=circle_radius, color='red', fill=False)
    plt.gcf().gca().add_artist(circle)

    plt.show()
# <--------------------------------------------------------

# -------------------------------------------------------->
def cont_update_test():
    x = np.linspace(0, 6 * np.pi, 100)
    y = np.sin(x)

    # You probably won't need this if you're embedding things in a tkinter plot...
    plt.ion()

    fig = plt.figure()
    ax = fig.add_subplot(111)
    line1, = ax.plot(x, y, 'r-')  # Returns a tuple of line objects, thus the comma

    for phase in np.linspace(0, 10 * np.pi, 500):
        line1.set_ydata(np.sin(x + phase))
        fig.canvas.draw()
        fig.canvas.flush_events()
# <--------------------------------------------------------

# END OF FUNCTION DEFINITIONS
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# BEGINNING OF MAIN
# GOAL: To create a single figure that continuously updates with new data

for item in location_list:
    get_centerpoint_location_for_plotting(item)
    #time.sleep(5)
'''
cont_update_test()
'''

# END OF MAIN
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
