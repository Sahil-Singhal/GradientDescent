# import numpy and pandas for data storage and calculations
import numpy as np
import pandas as pd

# import matplotlib for visualizations 
import matplotlib.pyplot as plt

# create an array 'x' with random values  
x = np.random.randn(100,1)

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
warr = np.empty(0)
barr = np.empty(0)
carr = np.empty(0)

iter = 10
for epoch in range(iter):
    w, b = descend(x, y, w, b, 0.01)
    predicted_y = w * x + b
    cost = np.sum((predicted_y - y)**2) / (2 * x.shape[0])
    carr = np.append(carr, cost)
    warr = np.append(warr, w)
    barr = np.append(barr, b)
    print(f"For iteration {epoch+1}, W was {round(w[0],4)}, B was {round(b[0],4)}, Cost was {round(cost,4)}")

index_with_min_cost = pd.Series(carr).idxmin()
optimal_w = warr[index_with_min_cost]
optimal_b = barr[index_with_min_cost]

predictions = optimal_w * x + optimal_b

plt.plot(predictions, c='blue', label='predicted values')
plt.plot(y, c='grey', label='actual values')
plt.legend()
plt.title(f"Comparison of Predictions and Actuals at {iter} iterations")
plt.savefig(f"{iter} iterations", dpi=300)
plt.show()
# repeat the above with 100 iterations
