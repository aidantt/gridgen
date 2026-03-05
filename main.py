# Project 1: Structured Mesh Generation
# Timofte, AERO 615

# Key Objectives:
# 1. import necessary libraries and initialize given values
# 2. construct an algebraic grid for (x,y) using the given boundary conditions
# 3. using the algebraic grid as an initial condition, solve the laplacian 
#    using Gauss-Seidel to obtain an improved orthogonal grid within tolerance

# module imports
from boundary_conditions import *
from visualization import plot_grid

# library imports
import numpy as np # for vector operations and fast arrays
import matplotlib.pyplot as plt # for grid visualization

# Step 1: initialize values ####################################################

# define Imax, Jmax, and tolerance
Imax = 5
Jmax = 5

tolerance = 1e-6

# Step 2: construct algebraic grid #############################################

# define mapping from (i,j) to (xi,eta) as equal spacings
xi, eta = np.meshgrid(np.linspace(0,1,Imax), np.linspace(0,1,Jmax))

# define algebraic mapping from (xi,eta) to (x,y)
x = xL + xi*(xR-xL)
y = yL(x) + eta*(yU(x) - yL(x))

# plot the x,y grid using the algebraic mapping
#plot_grid(x, y)

# Step 3: solve laplacian using Gauss-Seidel ###################################

# from the definition of xi, eta, calculate the discretized \Delta xi and eta
d_xi = 1/(Imax-1)
d_eta = 1/(Jmax-1)

# test the definitions above
#print(f'd_xi = {d_xi}, d_eta = {d_eta}')
#plot_grid(xi, eta)

# cast a grid x(i,j) into a 1D array of dimension Imax*Jmax
x_l = x.flatten(order='F') # column-major order

