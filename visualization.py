import numpy as np
import matplotlib.pyplot as plt

# define a function to plot a grid given a set of arrays
def plot_grid(xplot, yplot, name='grid', interactive=False):
    plt.figure()
    plt.plot(xplot, yplot, 'k-')
    plt.plot(np.transpose(xplot), np.transpose(yplot), 'k-')
    plt.xlim(-0.5, 5.5)
    plt.ylim(-0.5, 3.5)
    plt.savefig(f'{name}.png')
    if interactive:
        plt.show()
