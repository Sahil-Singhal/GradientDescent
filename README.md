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

<code></code>

Next, we need a dataset to work with. We will create an independant variable 'x' and a dependant variable 'y'.

<code></code>

Next we need to create a function to calculate the gradients of the cost function at specific values of 'w' and 'b'. 
We start with w and b at 0. 
Then calcuate the gradient and update 'w' and 'b'.

<code></code>

Finally, we repeat the process as many times as we want. I have shown results of 10 and 100 iterations. We can even run it a 1000 times.
Higher the number of iterations, the more accurate our predictions, but it also takes longer to run and needs more processing power. 

<code></code>

As expected, after 10 iterations, our predictions of 'y' are not even close to the actual 'y'.
But with 100 iterations, it is very close. 

And that's Gradient Descent !