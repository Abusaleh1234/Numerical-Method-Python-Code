import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import lineStyles

# a = float(input())
# b=float(input())
a= 0.0
b=0.8
Error = 1.640533  #given

def f(x):
    return 0.2+25*x-200*x**2+675*x**3-900*x**4+400*x**5

mid = (a+b)/2
I = (b-a)*(f(a)+4*f(mid)+f(b))/6
print("I = %.6f\n" %I)

#if error given
ExactError = ((Error - I)/Error)*100

print("Et = %.2f\n" %ExactError)

#ploting

x = np.linspace(a, b, 1000)
y = f(x)

# Plot the function
plt.plot(x, y, label='f(x)', color='blue')

# Highlighting the Simpson's 1/3 rule segments
xi = np.linspace(a, b, 10 + 1)
yi = f(xi)
for i in range(0, 10, 2):
    plt.fill_between([xi[i], xi[i + 2]], [yi[i], yi[i + 2]], color='lightblue', alpha=0.5)

plt.title("Simpson's 1/3 Rule Approximation")
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid()
plt.show()