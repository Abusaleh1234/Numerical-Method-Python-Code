import numpy as np
import matplotlib.pyplot as plt

# Define the function to integrate
def f(x):
    y= 0.2+25*x-200*x**2+675*x**3-900*x**4+400*x**5
    return y

# Trapezoidal Rule function
def trapezoidal_rule(f, a, b):
    return (b-a)*((f(a)+f(b))/2)

# Parameters
a = 0        # Lower limit
b = 0.8    # Upper limit

# Calculate integral using Trapezoidal Rule
integral_approx = trapezoidal_rule(f, a, b)
print(f"Approximate Integral: {integral_approx}")

# Plotting the function and trapezoidal approximation
x = np.linspace(a, b)
y = f(x)

# Plot the function
plt.plot(x, y, label='f(x) =y', color='blue')

xi = np.linspace(a, b, 10 + 1)
yi = f(xi)
for i in range(0, 10, 2):
    plt.fill_between([xi[i], xi[i + 2]], [yi[i], yi[i + 2]], color='lightblue', alpha=0.5)
    
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Trapezoidal Rule Approximation')
plt.legend()
plt.grid()
plt.show()
