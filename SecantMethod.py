import numpy as np
import matplotlib.pyplot as plt

def secant_method(f, x0, x1, tol=1e-5, max_iter=100):

    for _ in range(max_iter):
        if abs(f(x1) - f(x0)) < tol:
            print("Warning: Division by zero encountered.")
            return None
        x_new = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        
        if abs(x_new - x1) < tol:
            return x_new
        
        x0, x1 = x1, x_new
    
    print("Warning: Maximum iterations reached.")
    return x_new

# Example function: f(x) = x^2 - 2
def f(x):
    return x**3 + x - 1

# Initial guesses
x0 = 0
x1 = 1

# Finding the root
root = secant_method(f, x0, x1)
print(f"Root: {root}")

# Plotting the function
x = np.linspace(0, 2, 1000)
y = f(x)

plt.figure(figsize=(10,6))
plt.plot(x, y, label='f(x) = x^2 - 2', color='blue')
plt.axhline( color='black', lw=0.5)
plt.axvline(root, color='red', lw=0.5, label=f'Root Approx: {root:.4f}')
plt.title('Secant Method')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid()
plt.show()
