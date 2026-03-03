# Project 1: Structured Mesh Generation
# Timofte, AERO 615

# Key Objectives:
# 1. import necessary libraries and initialize given values
# 2. construct an algebraic grid for (x,y) using the given boundary conditions
# 3. using the algebraic grid as an initial condition, solve the laplacian 
#    using Gauss-Seidel to obtain an improved orthogonal grid within tolerance

import numpy as np
import matplotlib.pyplot as plt

# define Imax, Jmax, and tolerance
Imax = 50
Jmax = 10

tolerance = 1e-6

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

# define a function to plot a grid given a set of arrays
def plot_grid(xplot, yplot):
    plt.figure()
    plt.plot(xplot, yplot, 'k-')
    plt.plot(np.transpose(xplot), np.transpose(yplot), 'k-')
    plt.show()

# define mapping from (i,j) to (xi,eta) as equal spacings
xi, eta = np.meshgrid(np.linspace(0,1,Imax), np.linspace(0,1,Jmax))

# define mapping from (xi,eta) to (x,y)
x = xL + xi*(xR-xL)
y = yL(x) + eta*(yU(x) - yL(x))

# plot the x,y grid using the algebraic mapping
plot_grid(xi, eta)
plot_grid(x, y)
