# Project 1: Structured Mesh Generation
# Timofte, AERO 615

# Key Objectives:
# 1. import necessary libraries and initialize given values
# 2. construct an algebraic grid for (x,y) using the given boundary conditions
# 3. using the algebraic grid as an initial condition, solve the laplacian 
#    using Gauss-Seidel to obtain an improved orthogonal grid within tolerance

# module imports
from boundary_conditions import xL, xR, yL, yU
from visualization import plot_grid

# library imports
import numpy as np # for vector operations and fast arrays
import matplotlib.pyplot as plt # for grid visualization

# Step 1: initialize values ####################################################

# define Imax, Jmax, and tolerance
# i=j=0 is the upper left corner
# so, i increases downwards and j increases to the right
Imax = 11
Jmax = 51

tolerance = 1e-6
max_iter = 1e6

# variable conductivity cases
# 0: no clustering
# 1: linear function of eta, minimized at the top and maximized at the bottom
# 2: cosine wave over eta
# 3: sine wave over eta, maximized in the center
# 4: gaussian function in eta centered at eta=0.5 with sigma=0.1
CASE = 0

# Step 2: construct algebraic grid #############################################

# define mapping from (i,j) to (xi,eta) as equal spacings
# xi=eta=0 at the upper left corner
# xi increases to the right, eta increases downwards
xi, eta = np.meshgrid(np.linspace(0,1,Jmax), np.linspace(0,1,Imax))

# define algebraic mapping from (xi,eta) to (x,y)
x = xL + xi*(xR-xL)
y = yL(x) + eta*(yU(x) - yL(x))

# plot the x,y grid using the algebraic mapping
# plot_grid(xi, eta)
# plot_grid(x, y, name='algebraic_grid')

# Step 3: solve laplacian using Gauss-Seidel ###################################

# from the definition of xi, eta, calculate the discretized \Delta xi and eta
d_xi = 1/(Jmax-1)
d_eta = 1/(Imax-1)

# test the definitions above
# print(f'd_xi = {d_xi}, d_eta = {d_eta}')

# print(eta)
# print(eta.shape)

# initialize values for the iteration loop
iteration = 1
error = np.inf
alpha = np.zeros_like(x)
beta = np.zeros_like(x)
gamma = np.zeros_like(x)

# x = np.pad(x, pad_width=1, mode='edge')
# y = np.pad(y, pad_width=1, mode='edge')
x_old = x.copy()
y_old = y.copy()

while (error > tolerance):
    # loop through the interior points of the grid
    # outer points act as a boundary condition and are not updated
    for i in range(1, Imax-1):
        for j in range(1, Jmax-1):
            # calculate alpha, beta, gamma at the current point (i,j) using the definitions
            alpha[i,j] = 1/(4*d_eta**2) * \
                ( (x_old[i,j+1] - x_old[i,j-1])**2 + (y_old[i,j+1] - y_old[i,j-1])**2 )
            
            beta[i,j] = 1/(4*d_xi*d_eta) * \
                ( (x_old[i+1,j] - x_old[i-1,j])*(x_old[i,j+1] - x_old[i,j-1]) + \
                 (y_old[i+1,j] - y_old[i-1,j])*(y_old[i,j+1] - y_old[i,j-1]) )
            
            gamma[i,j] = 1/(4*d_xi**2) * \
                ( (x_old[i+1,j] - x_old[i-1,j])**2 + (y_old[i+1,j] - y_old[i-1,j])**2 )
            
            # calculate Gauss-Seidel coefficients
            a0 = 1 / ((2*alpha[i,j])/(d_xi)**2 + (2*gamma[i,j])/(d_eta)**2)
            a1 = (-1*beta[i,j])/(2*d_xi*d_eta) * a0
            a2 = (gamma[i,j])/(d_eta)**2 * a0
            a3 = (beta[i,j])/(2*d_xi*d_eta) * a0
            a4 = (alpha[i,j])/(d_xi)**2 * a0
            a5 = (alpha[i,j])/(d_xi)**2 * a0
            a6 = (beta[i,j])/(2*d_xi*d_eta) * a0
            a7 = (gamma[i,j])/(d_eta)**2 * a0
            a8 = (-1*beta[i,j])/(2*d_xi*d_eta) * a0

            # calculate varible conductivity k at the current point (i,j) based on the case
            if CASE == 0:
                k = np.ones_like(x)
            elif CASE == 1:
                k = 3 + eta**2
            elif CASE == 2:
                k = 0.5*np.cos(np.pi*eta) + 4
            elif CASE == 3:
                k = 1.0*np.sin(np.pi*eta) + 4
            elif CASE == 4:
                k = 0.5*np.exp(-((eta-0.5)**2)/(2*0.1**2)) + 1

            jacobian = 1/(4*d_xi*d_eta) * \
                ( (x_old[i,j+1] - x[i,j-1])*(y_old[i+1,j] - y[i-1,j]) \
                - (x_old[i+1,j] - x[i-1,j])*(y_old[i,j+1] - y[i,j-1]) )
            
            rhs_x = jacobian/(4*d_xi*d_eta*k[i,j]) * \
                ( (k[i,j+1] - k[i,j-1])*(y_old[i+1,j] - y[i-1,j]) \
                - (k[i+1,j] - k[i-1,j])*(y_old[i,j+1] - y[i,j-1]) )
            
            rhs_y = -1*jacobian/(4*d_xi*d_eta*k[i,j]) * \
                ( (k[i,j+1] - k[i,j-1])*(x_old[i+1,j] - x[i-1,j]) \
                - (k[i+1,j] - k[i-1,j])*(x_old[i,j+1] - x[i,j-1]) )

            variable_x = -1*rhs_x * a0
            variable_y = -1*rhs_y * a0

            # update x and y at the current point (i,j) using the Gauss-Seidel formula
            x[i,j] = a1*x[i-1,j-1] + a2*x[i-1,j] + a3*x[i-1,j+1] + a4*x[i,j-1] + \
                     a5*x_old[i,j+1] + a6*x_old[i+1,j-1] + a7*x_old[i+1,j] + a8*x_old[i+1,j+1] + \
                     variable_x
            
            y[i,j] = a1*y[i-1,j-1] + a2*y[i-1,j] + a3*y[i-1,j+1] + a4*y[i,j-1] + \
                     a5*y_old[i,j+1] + a6*y_old[i+1,j-1] + a7*y_old[i+1,j] + a8*y_old[i+1,j+1] + \
                     variable_y
    
    # calculate the error as the maximum change in x and y from the previous iteration
    error_x = np.max(np.abs(x - x_old))
    error_y = np.max(np.abs(y - y_old))
    error = max(error_x, error_y)

    # update values
    x_old = x.copy()
    y_old = y.copy()
    iteration += 1
    print(f'iteration: {iteration}, error: {error}')

# x = x[1:-1, 1:-1]
# y = y[1:-1, 1:-1]

# plot laplacian optimized grid
plot_grid(x,y, name='laplacian_grid', interactive=True)
