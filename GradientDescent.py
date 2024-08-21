Python 3.12.3 (v3.12.3:f6650f9ad7, Apr  9 2024, 08:18:48) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
================================ RESTART: Shell ================================
>>> 
================================ RESTART: Shell ================================
>>> def gradient_descent(X, y, theta, learning_rate, iterations):
...     m = len(y)
...     cost_history = np.zeros(iterations)
...     
...     for i in range(iterations):
...         gradients = X.T.dot(X.dot(theta) - y) / m
...         theta = theta - learning_rate * gradients
...         cost_history[i] = compute_cost(X, y, theta)
...     
...     return theta, cost_history
