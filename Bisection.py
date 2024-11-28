
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

m = 68.1  # mass in kg
g = 9.81  # gravitational acceleration in m/s^2
v = 40    # desired velocity in m/s
t = 10    # time in seconds
table_data = []

def bisection_method( a, b, tol=1e-5, max_itr = 100):
    if f(a) * f(b) >= 0.0:
        print("Bisection method fails. f(a) and f(b) must have opposite signs.")
        return -1

    for i in range(max_itr):
        # Midpoint
        c = (a + b) / 2
        f_a = f(a)
        f_b = f(b)
        f_c = f(c)
        # Append current iteration details to table data
        table_data.append([i+1, f"{a:.6f}", f"{b:.6f}", f"{c:.6f}", f"{f_a:.6f}", f"{f_b:.6f}", f"{f_c:.6f}"])

        if abs(f_c) == 0.0:
            break # Found the root

        # Narrow down the interval
        if f_b * f_c < 0:
            a = c
        else:
            b = c

    return table_data,c # Approximate root

# Example usage:
# Define the function whose root we want to find
def f(c):
    y = c**2 + 2*c -30   # Define the function you want to find the root for
    return y

# Define interval [a, b]
a = 4
b = 5
#tabulation

# Call the bisection method function
table_data,root = bisection_method( a, b)

print(tabulate(table_data,headers=["iteration","a","b","c(mid point)","f(a)","f(b)",'f(c)'],tablefmt="pretty"))

print("The root is:", root)

#ploting
x=np.linspace(-b,b)
y=f(x)
plt.plot(x,y,label='y=f(x)')
plt.scatter(root,f(root),label=f'root={root}',color = 'r')
plt.axhline(0,color='green',label='y=0')
plt.axvline(root,color='red',label=f' x = {root}')
plt.grid()
plt.title("bisection method")
plt.xlabel("x")
plt.ylabel("Y")
plt.legend()
plt.show()