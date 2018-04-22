###########################################################################################
###
### obj_detection_overlay.py
###
### nathan schram
###
### the purpose of this program is to plot a circle in red of diameter 15".
### the function will take the x, y location information for the center of the circle.
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
def get_centerpoint_location_for_plotting(location):

    print('Location: ', location)

    x_val = 'N/A';
    y_val = 'N/A';

    if (location == 'A'):
        x_val = a_circle[0]
        y_val = a_circle[1]
        print('---> x_val: ', x_val, " y_val: ", y_val)
    elif (location == 'B'):
        x_val = b_circle[0]
        y_val = b_circle[1]
        print('---> x_val: ', x_val, " y_val: ", y_val)
    elif (location == 'C'):
        x_val = c_circle[0]
        y_val = c_circle[1]
        print('---> x_val: ', x_val, " y_val: ", y_val)
    elif (location == 'D'):
        x_val = d_circle[0]
        y_val = d_circle[1]
        print('---> x_val: ', x_val, " y_val: ", y_val)
    elif (location == 'E'):
        x_val = e_circle[0]
        y_val = e_circle[1]
        print('---> x_val: ', x_val, " y_val: ", y_val)
    elif (location == 'F'):
        x_val = f_circle[0]
        y_val = f_circle[1]
        print('---> x_val: ', x_val, " y_val: ", y_val)
    elif (location == 'AB'):
        x_val = ab_circle[0]
        y_val = ab_circle[1]
        print('---> x_val: ', x_val, " y_val: ", y_val)
    elif (location == 'BC'):
        x_val = bc_circle[0]
        y_val = bc_circle[1]
        print('---> x_val: ', x_val, " y_val: ", y_val)
    elif (location == 'DE'):
        x_val = de_circle[0]
        y_val = de_circle[1]
        print('---> x_val: ', x_val, " y_val: ", y_val)
    elif (location == 'EF'):
        x_val = ef_circle[0]
        y_val = ef_circle[1]
        print('---> x_val: ', x_val, " y_val: ", y_val)
    elif (location == 'AD'):
        x_val = ad_circle[0]
        y_val = ad_circle[1]
        print('---> x_val: ', x_val, " y_val: ", y_val)
    elif (location == 'BE'):
        x_val = be_circle[0]
        y_val = be_circle[1]
        print('---> x_val: ', x_val, " y_val: ", y_val)
    elif (location == 'CF'):
        x_val = cf_circle[0]
        y_val = cf_circle[1]
        print('---> x_val: ', x_val, " y_val: ", y_val)
    elif (location == 'ABDF'):
        x_val = abdf_circle[0]
        y_val = abdf_circle[1]
        print('---> x_val: ', x_val, " y_val: ", y_val)
    elif (location == 'bcef'):
        x_val = bcef_circle[0]
        y_val = bcef_circle[1]
        print('---> x_val: ', x_val, " y_val: ", y_val)



    display_circle(x_val, y_val, circle_r)

    # -------------------------------------------------

def display_circle(x, y, circle_radius):

    fig = plt.figure()

    ax = fig.add_subplot(1, 1, 1)

    ax.axis('scaled')

    major_ticks_x = np.arange(0, global_x + 1, 5)
    minor_ticks_x = np.arange(0, global_x + 1, 1)

    major_ticks_y = np.arange(0, global_y + 1, 5)
    minor_ticks_y = np.arange(0, global_y + 1, 1)

    # v = [-global_x, global_x, -global_y, global_y]
    # ax.axis(v)/home/nathan/anaconda3/bin/python3.6 /home/nathan/PycharmProjects/ARS/Software/RTTM/obj_detection_overlay.py


    # ax.set_xlim(-global_x, global_x)
    # ax.set_ylim(-global_y, global_y)

    ax.set_xticks(major_ticks_x)
    ax.set_xticks(minor_ticks_x, minor=True)

    ax.set_yticks(major_ticks_y)
    ax.set_yticks(minor_ticks_y, minor=True)

    #ax.axis('scaled')
    # ax.plt.figure(figsize=(global_x, global_y))

    ax.grid(which='both')

    ax.grid(which='minor', alpha=0.2)
    ax.grid(which='major', alpha=0.5)

    circle = plt.Circle((x, y), linewidth=5, radius=circle_radius, color='red', fill=False)
    plt.gcf().gca().add_artist(circle)

    plt.show()


# ----------------------------------------------------------------------
# MAIN

for item in location_list:
    get_centerpoint_location_for_plotting(item)
    #time.sleep(5)
