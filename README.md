# LinearRegression-MLUdemycourse (I am uploading it quite late)
This is a basic coursework assignment I had done during my Udemy online course on Machine Learning. The task was to implement a basic machine learning algorithm from scratch to gain a deeper understanding of the underlying principles. It taught me how to implement the underlying principles of linear regression and gradient descent.

1. Understanding Linear Regression
Linear Regression is a supervised learning algorithm used to model the relationship between a dependent variable and one or more independent variables. The model attempts to predict the output using a linear equation:
y=θ0+θ1x1+θ2x2+⋯+θnxny = \theta_0 + \theta_1 x_1 + \theta_2 x_2 + \dots + \theta_n x_ny=θ0​+θ1​x1​+θ2​x2​+⋯+θn​x, where y is the predicted output,
x1, x2, x3...xn are the features and  
𝜃1...(theta)n are the model parameters.

2. Generating the Dataset
For simplicity, I used a synthetic dataset generated using numpy. The dataset consists of one feature and a corresponding output.

3. Defining the Hypothesis
The hypothesis (or model) is a simple linear function that predicts y based on the input features 𝑋.
The hypothesis for Linear Regression is: h0(X) = X.0 , where X is the input feature matrix, and 0(theta) is the parameter vector.

4. Cost Function
The cost function is used to measure the error between the predicted values and the actual values. For Linear Regression, we use the Mean Squared Error (MSE) as the cost function: J(θ)=2m1​i=1∑m​(hθ​(X(i))−y(i))2
where m is the number of training examples.

5.5. Gradient Descent
Gradient Descent is an optimization algorithm used to minimize the cost function. The idea is to start with an initial guess for the parameters and iteratively update them using the gradient of the cost function:
θ:=θ−α∂θ∂J(θ)​ , where α is the learning rate.

6. Training the Model
Next, I trained the model using the Gradient Descent algorithm, starting with an initial guess for the parameters and iterating until convergence.

7. Model Evaluation
After training, I evaluated the model by checking the final cost and comparing the model's predictions with the actual values.

8. Results
The model successfully fit the synthetic data, and the line of best fit closely matched the underlying data generation process. The plot generated shows the original data points and the line of best fit.
