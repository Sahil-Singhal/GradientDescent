# GradientDescent
Linear Regression is THE most popuar algorithm in machine learning. 
It uses Gradient Descent in the back end to find the line of best fit.
Infact, gradient descent is used by many popular algorithms, for example, logistic regression, neural network, and so on.

When we use sophisticated libraries like scikit learn to implement linear regression, gradient descent gets executed in the backend without being apparent. 
But as a practitioner of data science, it is important to understand the nuts and bolts of these libraries, in order to utilize them efficiently. 

In this article, I explain how to implement gradient descent on a linear regression problem. 
Let's dive right in. 

We start by importing the necessary libraries - numpy and pandas. 
We will also check whether gradient descent actually works by visualizing or predictons with actuals. 
For that, we need matplotlib.

<code>

Next, we need a dataset to work with. We can an independant variable 'x' and a dependant variable 'y'.
