Python 3.12.3 (v3.12.3:f6650f9ad7, Apr  9 2024, 08:18:48) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
================================ RESTART: Shell ================================
>>> 
================================ RESTART: Shell ================================
>>> 
================================ RESTART: Shell ================================
>>> # Initialize parameters
... theta = np.random.randn(2, 1)
... 
... # Set hyperparameters
... learning_rate = 0.01
... iterations = 1000
... 
... # Train the model
... theta, cost_history = gradient_descent(X_b, y, theta, learning_rate, iterations)
