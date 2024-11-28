import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Define symbols
x, y = sp.symbols('x y')

# Define the function f(x, y) in the differential equation y' = f(x, y)
f = x + y  # example function, change this as needed

# Initial conditions
x0 = 0  # initial x
y0 = 1  # initial y, y(x0) = y0

# Define the number of iterations for Picard's method
iterations = 4  # you can increase this for more accurate results

# Initialize y_n (Picard's iteration formula starts with y0 as the initial guess)
y_n = y0

# Perform iterations
for i in range(iterations):
    y_n = y0 + sp.integrate(f.subs(y, y_n), (x, x0, x))
    print(f"Iteration {i+1}: y{i+1} = {y_n}")

# Convert the final symbolic expression to a numerical function
y_n_func = sp.lambdify(x, y_n, modules="numpy")

# Plotting
x_vals = np.linspace(0, 5, 100)  # Adjust the range and number of points as needed
y_vals = y_n_func(x_vals)

plt.plot(x_vals, y_vals, label=f'Approx. solution after {iterations} iterations')
plt.xlabel('x')
plt.ylabel('y')
plt.title("Approximate Solution of Differential Equation using Picard's Iteration")
plt.legend()
plt.grid()
plt.show()
