import numpy as np
import pandas as pd

# Constants
m = 68.1      # mass of the parachutist in kg
v_target = 40 # target velocity in m/s
t = 10        # time in seconds
g = 9.81      # gravitational acceleration in m/s^2

# Define the function f(c) for which we want to find the root
def f(c):
    return (m * g / c) * (1 - np.exp(-c * t / m)) - v_target

# Bisection Method implementation
def bisection_method(f, a, b, tol=1e-5, max_iter=100):
    iteration_data = []  # Store data for each iteration
    iteration = 0
    while iteration < max_iter:
        c = (a + b) / 2
        fa, fb, fc = f(a), f(b), f(c)
        iteration_data.append({
            'Iteration': iteration,
            'a': a,
            'b': b,
            'c': c,
            'f(a)': fa,
            'f(b)': fb,
            'f(c)': fc
        })

        # Check if fc is close enough to zero
        if abs(fc) < tol:
            break  # Exit the loop if the root is found

        # Update interval based on the sign of fc
        if fa * fc < 0:
            b = c
        else:
            a = c

        iteration += 1

    # Return final midpoint if max iterations reached
    return (a + b) / 2, iteration_data

# Initial interval for c and tolerance
a, b = 12, 16  # Example interval
tol = 1e-5

# Perform the bisection method
root, data = bisection_method(f, a, b, tol)

# Create a DataFrame to show the results
results_df = pd.DataFrame(data)

# Display the DataFrame
print(results_df)
