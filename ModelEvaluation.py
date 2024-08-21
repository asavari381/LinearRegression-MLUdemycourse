Python 3.12.3 (v3.12.3:f6650f9ad7, Apr  9 2024, 08:18:48) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
================================ RESTART: Shell ================================
>>> 
================================ RESTART: Shell ================================
>>> 
================================ RESTART: Shell ================================
>>> 
================================ RESTART: Shell ================================
>>> # Final parameters
... print("Theta:", theta)
... 
... # Final cost
... print("Final cost:", cost_history[-1])
... 
... # Predictions
... predictions = X_b.dot(theta)
... 
... # Compare with actual values
... import matplotlib.pyplot as plt
... 
... plt.plot(X, y, 'b.')
... plt.plot(X, predictions, 'r-')
... plt.xlabel("X")
... plt.ylabel("y")
... plt.title("Linear Regression Fit")
... plt.show()
