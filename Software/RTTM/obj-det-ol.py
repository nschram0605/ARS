import matplotlib.pyplot as plt

def create_circle():
    circle=plt.Circle((0,0), alpha=0.5, radius=5) # alpha sets opaqueness
    return circle

def create_circle1():
    circle1=plt.Circle((0,0), color='r', radius=2)
    return circle1

def show_shape(patch):
    ax=plt.gca()
    ax.add_patch(patch)
    plt.axis('scaled')
    plt.show()

if __name__ =='__main__':
    c=create_circle()
    show_shape(c)
