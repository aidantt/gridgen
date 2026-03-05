import numpy as np

# define the boundary conditions
xL = 0
xR = 5

# define functions for the upper and lower y-boundaries as functions of x
# the input is a mesh of x-values, and the output is a mesh of y-values
def yL(x):
    y = np.zeros_like(x) # init
    # use vectorized booleans to define the piecewise function for yL
    y[(x >= 0) & (x <= 2)] = 0
    y[(x > 2) & (x <= 3)] = 0.17 * np.sin((x[(x > 2) & (x <= 3)] - 2) * np.pi)
    y[(x > 3) & (x <= 5)] = 0
    return y

def yU(x):
    y = np.zeros_like(x) # init
    y[(x >= 0) & (x <= 2)] = 1.0
    y[(x > 2) & (x <= 3)] = 1.0 - 0.17 * np.sin((x[(x > 2) & (x <= 3)] - 2) * np.pi)
    y[(x > 3) & (x <= 5)] = 1.0
    return y
