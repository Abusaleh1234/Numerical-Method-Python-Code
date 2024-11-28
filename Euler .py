import numpy as np
import matplotlib.pyplot as plt

# Define the differential equation dy/dx = f(x, y)
def f(x, y):
    return y - x**2 + 1

# Euler method
def euler_method(f, x0, y0, x_end, h):
    # Initialize variables
    x_values = [x0]
    y_values = [y0]
    
    # Perform Euler's method
    while x0 < x_end:
        y0 = y0 + h * f(x0, y0)
        x0 = x0 + h
        x_values.append(x0)
        y_values.append(y0)
        print(f"y{x0:.1f} = {y0}" ,'\n')
    return x_values, y_values

# Parameters
x0 = 0      # Initial x value
y0 = 0.5    # Initial y value
x_end = 2   # End of x interval
h = 0.1     # Step size

# Apply Euler's method
x_values, y_values = euler_method(f, x0, y0, x_end, h)
# Plot the results
plt.plot(x_values, y_values, label='Euler Approximation', marker='o', color='b')
# Plot settings
plt.xlabel('x')
plt.ylabel('y')
plt.title("Euler Method Approximation")
plt.legend()
plt.grid(True)
plt.show()
