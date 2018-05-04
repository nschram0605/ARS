###########################################################################################
###
### program: obj_detection_overlay.py
###
### author: n.schram
###
### date: 2018-APRL-21
###
### description: the purpose of this program is to plot a circle in red of diameter 8.5".
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

import numpy as np
import matplotlib.pyplot as plt
#from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import serial
import time
#import syslog


import scipy
import seaborn

# Position of circle, this comes from the detector circuit
# Object detection location: will change the location variable (A-F)
# Testing...
location = 'A'
location_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'N/A/']

# Detector circle dimensions in inches
circle_r = 4.25
circle_d = 8.5
circle_r_pixels = 192
circle_d_pixels = 384

# global sandbox size in inches & pixels
global_x = 40
global_y = 30
global_x_pixels = 1024
global_y_pixels = 768

# Define all position variables for circles in inches
# Total of 15 Detection Zones

a_circle = [5, 25]
b_circle = [15, 25]
c_circle = [25, 25]
d_circle = [35, 25]
e_circle = [5, 15]
f_circle = [15, 15]
g_circle = [25, 15]
h_circle = [35, 15]
i_circle = [5, 5]
j_circle = [15, 5]
k_circle = [25, 5]
l_circle = [35, 5]

# circle_r_pixels = 192

# pixel equivalent of 20: 512
# pixel equivalent of 22.5: 576
# pixel equivalent of 32.5: 832
'''
a_circle_pixels = [192, 576]
b_circle_pixels = [512, 576]
c_circle_pixels = [832, 576]
d_circle_pixels = [192, 192]
e_circle_pixels = [512, 192]
f_circle_pixels = [832, 192]
'''

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# BEGINNING OF FUNCTION DEFINITIONS.

# -------------------------------------------------------->
def get_centerpoint_location_for_plotting(location):


    local_label = 'N/A'
    global x_val
    global y_val

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
    elif (location == 'G'):
        print('Location: ', location)
        location_label = 'G'
        x_val = g_circle[0]
        y_val = g_circle[1]
        print('---> x_val: ', x_val, " y_val: ", y_val)
    elif (location == 'H'):
        print('Location: ', location)
        location_label = 'H'
        x_val = h_circle[0]
        y_val = h_circle[1]
        print('---> x_val: ', x_val, " y_val: ", y_val)
    elif (location == 'I'):
        print('Location: ', location)
        location_label = 'I'
        x_val = i_circle[0]
        y_val = i_circle[1]
        print('---> x_val: ', x_val, " y_val: ", y_val)
    elif (location == 'J'):
        print('Location: ', location)
        location_label = 'J'
        x_val = j_circle[0]
        y_val = j_circle[1]
        print('---> x_val: ', x_val, " y_val: ", y_val)
    elif (location == 'K'):
        print('Location: ', location)
        location_label = 'K'
        x_val = k_circle[0]
        y_val = k_circle[1]
        print('---> x_val: ', x_val, " y_val: ", y_val)
    elif (location == 'L'):
        print('Location: ', location)
        location_label = 'L'
        x_val = l_circle[0]
        y_val = l_circle[1]
        print('---> x_val: ', x_val, " y_val: ", y_val)
    elif (location == 'N/A'):
        print('NO DETECTIONS')
        location_label = 'N/A'
        x_val = 0
        y_val = 0
        print('---> x_val: ', x_val, " y_val: ", y_val)

    display_circle_cont(x_val, y_val, circle_r, location_label)
    #display_circle_stepthrough(x_val, y_val, circle_r, location_label)
    #update_plot(x_val, y_val, circle_r, location_label)

# <--------------------------------------------------------

# -------------------------------------------------------->
def get_serial_data():

    nix_port = '/dev/ttyACM0'
    #win_port = '/dev/tty.usbserial'
    #win_port = 'com3'
    serial_interface = serial.Serial(nix_port, 115200, timeout=50)
    serial_data = str(serial_interface.readline())
    #serial_interface.close()
    #print("[Arduino Mega] :", serial_data)
    print(serial_data)
    serial_interface.flush()
    return serial_data

# <--------------------------------------------------------


# -------------------------------------------------------->
def parse_serial_data(serial_string):
    prefix = "b'"
    postfix = '\\r\\n'
    combined = prefix + serial_string + postfix
    parsed_string = 'N/A'
    '''
    print("prefix: ", prefix)
    print("postfix: ", postfix)
    print("combined: ", combined)
    '''
    #rint(serial_string)
    #print("serial_string: ", serial_string)
    #print("combined str : ", combined)

    if (serial_string == "b'A\\r\\n'"):
        parsed_string = 'A'
        #print("A")

    if (serial_string == "b'B\\r\\n'"):
        parsed_string = 'B'
        # print("B")

    if (serial_string == "b'C\\r\\n'"):
        parsed_string = 'C'
        # print("C")

    if (serial_string == "b'D\\r\\n'"):
        parsed_string = 'D'
        # print("D")

    if (serial_string == "b'E\\r\\n'"):
        parsed_string = 'E'
        # print("E")

    if (serial_string == "b'F\\r\\n'"):
        parsed_string = 'F'
        # print("F")

    if (serial_string == "b'G\\r\\n'"):
        parsed_string = 'G'
        # print("G")

    if (serial_string == "b'H\\r\\n'"):
        parsed_string = 'H'
        # print("H")

    if (serial_string == "b'I\\r\\n'"):
        parsed_string = 'I'
        # print("I")

    if (serial_string == "b'J\\r\\n'"):
        parsed_string = 'J'
        # print("J")

    if (serial_string == "b'K\\r\\n'"):
        parsed_string = 'K'
        # print("K")

    if (serial_string == "b'L\\r\\n'"):
        parsed_string = 'L'
        # print("L")

    if (serial_string == "b'N/A\\r\\n'"):
        parsed_string = 'N/A'
        #print("N/A")

    #print(parsed_string)

    return parsed_string

# <--------------------------------------------------------


# --------------------------------------------------------->
def display_circle_stepthrough(x, y, circle_radius, label_location):

    #plt.cla()

    fig = plt.figure()

    #fig.figure(figsize=(40, 30))

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

    plt.title(label_location)

    if x==0 and y==0:
        plt.show()
        #plt.imshow(left=1.0, right=1.0, bottom=1.0, top=1.0)
    else:
        circle = plt.Circle((x, y), linewidth=5, radius=circle_radius, color='red', fill=False)
        plt.gcf().gca().add_artist(circle)
        plt.show()
        plt.cla()
        #plt.imshow(left=0.0, right=1.0, bottom=0.0, top=1.0)

# <--------------------------------------------------------

# --------------------------------------------------------->
def display_circle_cont(x, y, circle_radius, label_location):

    #plt.ion()

    fig = plt.figure()

    ax = fig.add_subplot(1, 1, 1)
    #ax = fig.add_subplot(111)

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


    if label_location == 'A':
        #plt.cla()
        circle_a = plt.Circle((a_circle[0], a_circle[1]), linewidth=5, radius=circle_r, color='red', fill=False)
        plt.gcf().gca().add_artist(circle_a)
        #plt.show()
        #plt.cla()

    #if label_location == 'N/A':
        #plt.cla()
        #plt.show()
        #plt.cla()

    #circle = plt.Circle((x, y), linewidth=5, radius=circle_radius, color='red', fill=False)
    #plt.gcf().gca().add_artist(circle)
    plt.figure(figsize=(40, 30))
    plt.tight_layout()
    #plt.subplots_adjust(left=1, right=2, top=2, bottom=1)
    plt.show()
# <--------------------------------------------------------

# -------------------------------------------------------->
def update_plot(x, y, circle_r, label_location):


    '''
    if label_location == 'A':
        #plt.cla()
        circle_a = plt.Circle((a_circle[0], a_circle[1]), linewidth=5, radius=circle_r, color='red', fill=False)
        plt.gcf().gca().add_artist(circle_a)
        #plt.pause(1)
        #plt.show()

    if label_location == 'B':
        #plt.cla()
        circle_b = plt.Circle((b_circle[0], b_circle[1]), linewidth=5, radius=circle_r, color='red', fill=False)
        plt.gcf().gca().add_artist(circle_b)
        #plt.pause(1)
        #plt.show()

    if label_location == 'C':
        #plt.cla()
        circle_c = plt.Circle((c_circle[0], c_circle[1]), linewidth=5, radius=circle_r, color='red', fill=False)
        plt.gcf().gca().add_artist(circle_c)
        #plt.pause(1)
        #plt.show()

    if label_location == 'D':
        #plt.cla()
        circle_d = plt.Circle((d_circle[0], d_circle[1]), linewidth=5, radius=circle_r, color='red', fill=False)
        plt.gcf().gca().add_artist(circle_d)
        #plt.pause(1)
        #plt.show()

    if label_location == 'E':
        #plt.cla()
        circle_e = plt.Circle((e_circle[0], e_circle[1]), linewidth=5, radius=circle_r, color='red', fill=False)
        plt.gcf().gca().add_artist(circle_e)
        #plt.pause(1)
        #plt.show()

    if label_location == 'F':
        #plt.cla()
        circle_f = plt.Circle((f_circle[0], f_circle[1]), linewidth=5, radius=circle_r, color='red', fill=False)
        plt.gcf().gca().add_artist(circle_f)
        #plt.pause(1)
        #plt.show()

    if label_location == 'G':
        #plt.cla()
        circle_g = plt.Circle((g_circle[0], g_circle[1]), linewidth=5, radius=circle_r, color='red', fill=False)
        plt.gcf().gca().add_artist(circle_g)
        #plt.pause(1)
        #plt.show()

    if label_location == 'H':
        #plt.cla()
        circle_h = plt.Circle((h_circle[0], h_circle[1]), linewidth=5, radius=circle_r, color='red', fill=False)
        plt.gcf().gca().add_artist(circle_h)
        #plt.pause(1)
        #plt.show()

    if label_location == 'I':
        plt.cla()
        circle_i = plt.Circle((i_circle[0], i_circle[1]), linewidth=5, radius=circle_r, color='red', fill=False)
        plt.gcf().gca().add_artist(circle_i)
        #plt.pause(1)
        #plt.show()

    if label_location == 'J':
        #plt.cla()
        circle_j = plt.Circle((j_circle[0], j_circle[1]), linewidth=5, radius=circle_r, color='red', fill=False)
        plt.gcf().gca().add_artist(circle_j)
        #plt.pause(1)
        #plt.show()

    if label_location == 'K':
        #plt.cla()
        circle_k = plt.Circle((k_circle[0], k_circle[1]), linewidth=5, radius=circle_r, color='red', fill=False)
        plt.gcf().gca().add_artist(circle_k)
        #plt.pause(1)
        #plt.show()

    if label_location == 'L':
        #plt.cla()
        circle_l = plt.Circle((l_circle[0], l_circle[1]), linewidth=5, radius=circle_r, color='red', fill=False)
        plt.gcf().gca().add_artist(circle_l)
        #plt.pause(1)
        #plt.show()

    #if label_location == 'N/A':
    #    circle_a = plt.Circle((a_circle[0], a_circle[1]), linewidth=5, radius=circle_r, color='red', fill=False)
    #    plt.gcf().gca().add_artist(circle_a)
    #    plt.pause(1)
    #    plt.show()
    #    plt.cla()

    #plt.show()
    '''
    


# <--------------------------------------------------------

# -------------------------------------------------------->
def display_all_locations():

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

    # plt.title('Location: ', label_location)

    circle_a = plt.Circle((a_circle[0], a_circle[1]), linewidth=5, radius=circle_r, color='red', fill=False)
    circle_b = plt.Circle((b_circle[0], b_circle[1]), linewidth=5, radius=circle_r, color='red', fill=False)
    circle_c = plt.Circle((c_circle[0], c_circle[1]), linewidth=5, radius=circle_r, color='red', fill=False)
    circle_d = plt.Circle((d_circle[0], d_circle[1]), linewidth=5, radius=circle_r, color='red', fill=False)
    circle_e = plt.Circle((e_circle[0], e_circle[1]), linewidth=5, radius=circle_r, color='red', fill=False)
    circle_f = plt.Circle((f_circle[0], f_circle[1]), linewidth=5, radius=circle_r, color='red', fill=False)
    circle_g = plt.Circle((g_circle[0], g_circle[1]), linewidth=5, radius=circle_r, color='red', fill=False)
    circle_h = plt.Circle((h_circle[0], h_circle[1]), linewidth=5, radius=circle_r, color='red', fill=False)
    circle_i = plt.Circle((i_circle[0], i_circle[1]), linewidth=5, radius=circle_r, color='red', fill=False)
    circle_j = plt.Circle((j_circle[0], j_circle[1]), linewidth=5, radius=circle_r, color='red', fill=False)
    circle_k = plt.Circle((k_circle[0], k_circle[1]), linewidth=5, radius=circle_r, color='red', fill=False)
    circle_l = plt.Circle((l_circle[0], l_circle[1]), linewidth=5, radius=circle_r, color='red', fill=False)

    plt.gcf().gca().add_artist(circle_a)
    plt.gcf().gca().add_artist(circle_b)
    plt.gcf().gca().add_artist(circle_c)
    plt.gcf().gca().add_artist(circle_d)
    plt.gcf().gca().add_artist(circle_e)
    plt.gcf().gca().add_artist(circle_f)
    plt.gcf().gca().add_artist(circle_g)
    plt.gcf().gca().add_artist(circle_h)
    plt.gcf().gca().add_artist(circle_i)
    plt.gcf().gca().add_artist(circle_j)
    plt.gcf().gca().add_artist(circle_k)
    plt.gcf().gca().add_artist(circle_l)

    plt.show()


# <--------------------------------------------------------


# END OF FUNCTION DEFINITIONS
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# BEGINNING OF MAIN
# GOAL: To create a single figure that continuously updates with new data

#fig = plt.gcf()
#fig.show()
#fig.canvas.draw(

zone = 'A'

while 1:

    #zone = parse_serial_data(get_serial_data())
    #print(zone)
    get_centerpoint_location_for_plotting(zone)




# END OF MAIN
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
