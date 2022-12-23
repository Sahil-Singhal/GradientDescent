# import numpy and pandas for data storage and calculations
import numpy as np
import pandas as pd

# import matplotlib for visualizations 
import matplotlib.pyplot as plt

# create an array 'x' with random values  
x = np.random.randn(10,1)

# create a dependent array 'y' with slope 'x' and a random variable as constant 
y = 5 * x + np.random.rand()

# a straight line equation is represented as 'wx + b'
# where 'w' is the slope or the factor by which 'y' changes wrt 'x'
# let's initialize 'w' and 'b' as 0 to start with 

w = 0
b = 0

# write a function to calculate the partial derivative of 'w' and 'b' 
def descend(x, y, w, b, alpha):
    # first let's initialize partial deriative of 'w' and 'b'
    dldw = 0.0
    dldb = 0.0
    # 'N' refers to the number of values in the 'x' variable 
    N = x.shape[0]
    for xi, yi in zip(x, y):
        dldw += -2 * xi * (yi - (w * xi + b))
        dldb += -2 * (yi - (w * xi + b))
    w = w - dldw * alpha / N
    b = b - dldb * alpha / N
    return w, b
    
# run iterations to reach the lowest cost or find the optimum solutions
for epoch in range(500):
    w, b = descend(x, y, w, b, 0.01)
    predicted_y = w * x + b
    cost = np.sum((predicted_y - y)**2) / (2 * x.shape[0])
    print(f"For iteration {epoch+1}, W was {round(w[0],4)}, B was {round(b[0],4)}, Cost was {round(cost,4)}")