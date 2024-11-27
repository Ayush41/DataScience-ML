# IMPLEMENTING Linear Regression from Scratch

# Objective: Implement a simple linear regression model from scratch using randomly generated data.

import numpy as np
import matplotlib.pyplot as pllt

#generating random data
# Independent variable
X = np.random.rand(100,1) *10 #
# Dependent variable
Y = 3*X + np.random.randn(100,1) *2

# LInear regression

X_b = np.c_[np.ones((100,1)),X] 
theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(Y)

# pridict values
Y_pred = X_b.dot(theta_best)

# Plottting graph
pllt.scatter(X,Y,color="Blue",label="Data Points")
pllt.plot(X,Y_pred,color="Red",label="Regression Line")

pllt.xlabel("X")
pllt.ylabel("Y")
pllt.legend()
pllt.show