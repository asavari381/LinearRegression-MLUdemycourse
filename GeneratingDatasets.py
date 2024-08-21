Python 3.12.3 (v3.12.3:f6650f9ad7, Apr  9 2024, 08:18:48) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
================================ RESTART: Shell ================================
>>> import numpy as np
... 
... # Generate a synthetic dataset
... np.random.seed(0)
... X = 2 * np.random.rand(100, 1)
... y = 4 + 3 * X + np.random.randn(100, 1)
... 
... # Add the bias term (x_0 = 1)
... X_b = np.c_[np.ones((100, 1)), X]
