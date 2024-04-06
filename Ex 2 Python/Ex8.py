'''
Write a program that draws the basic trigonometric functions over a meaningful domain, 
using NumPy universal functions

*Show that the sin and cosin functions differ by a phase

*Show that the terms A and B in the equation sin(x-A) + B
 represent horizontal and vertical translations of the functional form, respectively

Show that the terms C and D in the equation Dcos(Cx)
 represent horizontal and vertical dilations of the functional form, respectivey


'''
import numpy as np
import matplotlib.pyplot as plt

def func1(x):
    return np.sin(x-np.pi) + 1

def func2(x):
    return 3*np.cos(2*x)

def main():
    x_coord = np.linspace(0,2*np.pi,10_000)
    y1_coord = np.sin(x_coord)
    y2_coord = np.cos(x_coord)
    y3_coord = func1(x_coord)
    y4_coord = func2(x_coord)

    fig, ax = plt.subplots(3,1)

    ax[0].plot(x_coord,y1_coord,label = 'sin(x)')
    ax[0].plot(x_coord,y2_coord, label = 'cos(x)')
    ax[0].set_xlabel('x')
    ax[0].set_ylabel('f(x)')
    ax[0].set_title('Shift Cos(x) e Sin(x)')
    ax[0].legend()
    
    
    ax[1].plot(x_coord,y1_coord,label = 'sin(x)')
    ax[1].plot(x_coord,y3_coord,label = 'sin(x-pi) + 1')
    ax[1].set_xlabel('x')
    ax[1].set_ylabel('f(x)')
    ax[1].set_title('Shift horizontal and vertical for sin(x) function')
    ax[1].legend()
    
    ax[2].plot(x_coord,y1_coord,label = 'sin(x)')
    ax[2].plot(x_coord,y4_coord,label = '3cos(2x)')
    ax[2].set_xlabel('x')
    ax[2].set_ylabel('f(x)')
    ax[2].set_title('Horizontal and vertical dilatation for cos(x) function')
    ax[2].legend()
    
    fig.tight_layout(pad=0.3)
    plt.show()
    return

if __name__ == '__main__':
    main()