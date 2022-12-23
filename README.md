# Gradient Descent
Linear Regression is THE most popuar algorithm in machine learning. 
It uses Gradient Descent in the back end to find the line of best fit.
Infact, gradient descent is used by many popular algorithms, for example, logistic regression, neural network, and so on.

When we use sophisticated libraries like scikit learn to implement linear regression, gradient descent gets executed in the backend without being apparent. 
But as a practitioner of data science, it is important to understand the nuts and bolts of these libraries, in order to utilize them efficiently. 

In this article, I explain how to implement gradient descent on a linear regression problem. 
Let's dive right in. 

We start by importing the necessary libraries - numpy and pandas. 
We will also check whether gradient descent actually works by visualizing our predictons with actuals. 
For that, we need matplotlib.

```python
import numpy as np
import pandas as pd

# import matplotlib for visualizations 
import matplotlib.pyplot as plt
```

Next, we need a dataset to work with. We will create an independant variable 'x' and a dependant variable 'y'.

```python
# create an array 'x' with random values  
x = np.random.randn(10,1)

# create a dependent array 'y' with slope 'x' and a random variable as constant 
y = 5 * x + np.random.rand()
```

Next we need to create a function to calculate the gradients of the cost function at specific values of 'w' and 'b'. 
We start with w and b at 0. 
Then calcuate the gradient and update 'w' and 'b'.

```python
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
```

Finally, we repeat the process as many times as we want. I have shown results of 10 and 100 iterations. We can even run it a 1000 times.
Higher the number of iterations, the more accurate our predictions, but it also takes longer to run and needs more processing power. 

```python
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
```

As expected, after 10 iterations, our predictions of 'y' are not even close to the actual 'y'.
But with 100 iterations, it is very close. 

![image](https://user-images.githubusercontent.com/113739146/209274587-950c9d29-a115-466d-9aac-42dcd1e0d835.png)
![image](https://user-images.githubusercontent.com/113739146/209274600-f049a570-1f01-4e17-9da6-144196f8f935.png)

And that's Gradient Descent !
