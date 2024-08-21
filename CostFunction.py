Python 3.12.3 (v3.12.3:f6650f9ad7, Apr  9 2024, 08:18:48) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
================================ RESTART: Shell ================================
>>> def compute_cost(X, y, theta):
...     m = len(y)
...     predictions = X.dot(theta)
...     cost = (1/2*m) * np.sum(np.square(predictions - y))
...     return cost
