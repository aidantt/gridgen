import numpy as np
import matplotlib.pyplot as plt

# define a function to plot a grid given a set of arrays
def plot_grid(xplot, yplot):
    plt.figure()
    plt.plot(xplot, yplot, 'k-')
    plt.plot(np.transpose(xplot), np.transpose(yplot), 'k-')
    plt.show()
