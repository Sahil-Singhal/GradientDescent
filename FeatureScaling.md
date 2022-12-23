# Why scale? 
Usually, a dataset has features (variables) with varying ranges. 
For example, imagine a dataset with Age and Height of students of primary school.
- Age(yrs): ranges between 5 and 15
- Height(cm): ranges between 100 to 180
If we were to plot these on a 2D chart, it would look something like so-
IMG_0364.JPG

And the cost function for a linear regression with these two features would look something like so. 
image

Notice the long ZIG-ZAG path taken by the algorithm to find the local minimum. This is because even a one unit change in Age makes the algorithm jump around more than what's ideal. Whereas one unit change in Height does not impact the cost as much. 
Post feature scaling, the 2 features are distributed more evenly. 
image

The algorithm now follows a much shorter straighter path to reach the local minimum. 
image

While we can find the local minimum with and without feature scaling, scaling makes the process more cost and time efficient. Hence, it is recommended. 