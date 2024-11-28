import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate


def runge_kutta_4th_order(f, x0, y0, x_end, h):
 
    # Initialize variables
    x_values = [x0]
    y_values = [y0]
    x = x0
    y = y0
    
    # Runge-Kutta loop
    while x < x_end:
        # Calculate the four slopes
        k1 = h * f(x, y)
        k2 = h * f(x + h/2, y + k1/2)
        k3 = h * f(x + h/2, y + k2/2)
        k4 = h * f(x + h, y + k3)
        
        # Update y and x values
        y = y + (k1 + 2*k2 + 2*k3 + k4) / 6
        x = x + h
        
        # Store values
        x_values.append(x)
        y_values.append(y)
    
    return x_values,y_values

# Example usage
# Define the differential equation dy/dx = f(x, y)
def f(x, y):
    return x + y  # Example: dy/dx = x + y

# Initial conditions and parameters
x0 = 0      # Initial x-value
y0 = 1      # Initial y-value (initial condition y(x0) = 1)
x_end = 2   # Endpoint for x
h = 0.1     # Step size
# Solve the differential equation using RK4
x_values, y_values = runge_kutta_4th_order(f, x0, y0, x_end, h)

# Print or plot the results
# print(f"stepNo\t\t X\t\tY")
# for i in range(len(x_values)):
#     print(f'{i}\t\t{x_values[i]:.3f}\t\t{y_values[i]:.3f}')
table_data = []
for i in range(len(x_values)):
    table_data.append([f"{x_values[i]:.2f}", f"{y_values[i]:.4f}"])

# Print results in tabular form
print(tabulate(table_data, headers=["x", "y"], tablefmt="pretty"))

#ploting
plt.plot(x_values,y_values,label='Y=f(x)',marker='o')
plt.scatter(x_values[len(x_values)-1],y_values[len(y_values)-1],color = 'red')
plt.axvline(x_values[len(x_values)-1],lw='0.5')
plt.axhline(y_values[len(x_values)-1],lw='0.5')
plt.show()