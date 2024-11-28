import numpy as np
import matplotlib.pyplot as plt

# Given data
x = np.array([1,2,3,4,5,6,7])
y = np.array([0.5,2.5,2.0,4.0,3.5,6.0,5.5])

# Number of data points
N = len(x)

# Calculate sums
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_xy = np.sum(x * y)
sum_x_squared = np.sum(x ** 2)

# Calculate slope (m) and intercept (b)
slope = (N * sum_xy - sum_x * sum_y) / (N * sum_x_squared - sum_x ** 2)
intercept = (sum_y - slope * sum_x) / N

# Print the equation of the line
print(f"Equation of the line: y = {intercept:.2f} + {slope:.2f}x")

# Define the line function
def line(x):
    return intercept + slope * x

# Generate points for the line of best fit
x_line = np.linspace(min(x), max(x), 100)
y_line = line(x_line)

# Plot data points
plt.scatter(x, y, color='blue', label='Data Points')

# Plot line of best fit
plt.plot(x_line, y_line, color='red', label=f'Best-Fit Line: y = {intercept:.2f} + {slope:.2f}x')

# Plot settings
plt.xlabel('x')
plt.ylabel('y')
plt.title('Least Squares Line of Best Fit')
plt.legend()
plt.grid(True)
plt.show()
