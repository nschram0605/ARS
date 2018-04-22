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
a_circle = [7.5, 22.5]
b_circle = [20, 22.5]
c_circle = [32.5, 22.5]
d_circle = [7.5, 7.5]
e_circle = [20, 7.5]
f_circle = [32.5, 7.5]

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

    print ('Location: ', location)

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
        x_val = e_cirlce[0]
        y_val = e_circle[1]
        print('---> x_val: ', x_val, " y_val: ", y_val)
    elif (location == 'F'):
        x_val = f_circle[0]
        y_val = f_circle[1]
        print('---> x_val: ', x_val, " y_val: ", y_val)

    #plot_detection_circle(x_val, y_val, circle_r)
    create_test_grid(x_val, y_val, circle_r)

    # ------------------------------------------------->

def create_grid():

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    major_ticks_x = np.arange(0, global_x + 1, 5)
    minor_ticks_x = np.arange(0, global_x + 1, 1)

    major_ticks_y = np.arange(0, global_y + 1, 5)
    minor_ticks_y = np.arange(0, global_y + 1, 1)

    # v = [-global_x, global_x, -global_y, global_y]
    # ax.axis(v)

    # ax.set_xlim(-global_x, global_x)
    # ax.set_ylim(-global_y, global_y)

    ax.set_xticks(major_ticks_x)
    ax.set_xticks(minor_ticks_x, minor=True)

    ax.set_yticks(major_ticks_y)
    ax.set_yticks(minor_ticks_y, minor=True)

    # ax.axis('scaled')

    ax.grid(which='both')

    ax.grid(which='minor', alpha=0.2)
    ax.grid(which='major', alpha=0.5)

    plt.show()


def create_test_grid(x, y, circle_radius):

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

def plot_detection_circle(x, y, circle_radius):

    '''
    plt.axes()
    circle = plt.Circle((x, y), linewidth=5, radius=circle_radius, color='red', fill=False)
    # .figure(figsize=(global_x, global_y))
    # plt.figure(figsize=(global_x, global_y))
    v = [-global_x, global_x, -global_y, global_y]

    plt.gca().add_patch(circle)
    plt.axis('scaled')
    plt.axis(v)
    plt.grid(True)
    plt.title('Object Detection')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.show()
    '''

'''
    print ("X: ", x, " Y: ", y, " Circle Radius (in.): ", circle_radius)

    circle1 = plt.Circle((x, y), circle_radius, color='red', fill=False)

    #fig, ax = plt.subplots()  # note we must use plt.subplots, not plt.subplot
    #plt.figure(figsize=(global_x, global_y))
    print("Sandbox Dimensions:", global_x, "x", global_y)
    plt.figure(num=1, figsize=(global_x, global_y), facecolor='w')
    plt.gcf().gca().add_artist(circle1)

    # for existing figure
    # plt.gcf().gca().add_artist(circle1)
    # (or if you have an existing figure)
    # fig = plt.gcf()
    # ax = fig.gca()
    plt.grid(True)
    # plt.figure(figsize=(x, y))
    #ax.add_artist(circle1)

    plt.show()
    #fig.savefig('plotcircles.png')


    #plt.figure()
    #ax1 = fig1.add_subplot(111, aspect='equal')

    #circle = plt.Circle((0.5, 0.5), radius=circle_radius, color='red', fill=False)
    #circle = plt.Circle((x, y), radius=circle_radius, color='red', fill=False)
    #fig, ax = plt.subplots()
    #ax.add_artist(circle)
    #plt.show()
    #ax = plt.gca()
    #ax.cla()
    #ax.add_artist(circle)
    #ax.show()

    # plt.plot(circle)
    # plt.figure(1, figsize=(L,W))
    # plt.figure(figsize=(4, 3))
    # plt.figure(figsize=(40, 30), dpi=500)
    #plt.xlabel('X Axis (In.)')
    #plt.ylabel('Y Axis (In.)')
    #plt.title('Object Detection')
    #plt.grid(True)
    # plt.savefig("sin_wave.png", transparent=True)
    #plt.show()
    return
'''
# <-------------------------------------------------

'''
def create_circle():
    circle=plt.Circle(0,0), radius=5)
    return circle

def show_shape(patch):
    ax=plt.gca()
    ax.add_patch(patch)
    plt.axis('scaled')
    plt.show()
'''
# ----------------------------------------------------------------------

get_centerpoint_location_for_plotting(location)

#create_grid()
#plot_detection_circle(4, 3, 10)

#c=create_circle()
#show_shape(c)

#create_test_grid()

'''
plt.axes()
circle = plt.Circle((0, 0), linewidth=5, radius=0.75, color='red', fill=False)
#.figure(figsize=(global_x, global_y))
#plt.figure(figsize=(global_x, global_y))
v = [-global_x, global_x, -global_y, global_y]

plt.gca().add_patch(circle)
plt.axis('scaled')
plt.axis(v)
plt.grid(True)
plt.title('Object Detection')
plt.xlabel('X Axis')
plt.ylabel('Y Ax
'''