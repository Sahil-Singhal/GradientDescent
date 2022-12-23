# Feature Scaling
## Why do you need it? 
Usually, a dataset has features (variables) with varying ranges. 

For example, imagine a dataset with Age and Height of students of primary school.
- Age(yrs): ranges between 5 and 15
- Height(cm): ranges between 100 to 180

If we were to plot these on a 2D chart, it would look something like so-

![image](https://user-images.githubusercontent.com/113739146/209323916-264f16de-bba0-414a-b193-eb952e78b1c5.png)

And the cost function for a linear regression with these two features would look something like so. 

![image](https://user-images.githubusercontent.com/113739146/209323927-e442aa0a-ab1e-4024-ac02-a47ea8c3efe5.png)


Notice the long ZIG-ZAG path taken by the algorithm to find the local minimum. This is because even a one unit change in Age makes the algorithm jump around more than what's ideal. Whereas one unit change in Height does not impact the cost as much. 

Post feature scaling, the 2 features are distributed more evenly. 

![image](https://user-images.githubusercontent.com/113739146/209323949-88b64b99-8661-47b8-909d-b3dc766ec60d.png)

The algorithm now follows a much shorter straighter path to reach the local minimum. 

![image](https://user-images.githubusercontent.com/113739146/209323965-bd7228f9-26fe-4d24-81ea-b239bb99888e.png)

While we can find the local minimum with and without feature scaling, scaling makes the process more cost and time efficient. Hence, it is recommended. 
