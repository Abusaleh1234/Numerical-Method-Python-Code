import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
import math

table_data = []
a = 0
b = 1

def func( x ):
    return 2*np.exp(x)*np.sin(x)-3

# Prints root of func(x) in interval [a, b]
def regulaFalsi( a , b,MAX_ITER = 100):
    print(func(a),'\n',func(func(b)),'\n')
    if func(a) * func(b) >= 0.0:
        print("You have not assumed right a and b")
        return -1
    
    c = a # Initialize result
    
    for i in range(MAX_ITER):
        
        # Find the point that touches x axis
        c = (a * func(b) - b * func(a))/ (func(b) - func(a))

        f_a = func(a)
        f_b = func(b)
        f_c = func(c)

        table_data.append([f'{i+1}',f'{a:.3f}',f'{b:.3f}',f'{c:.3f}',f'{f_a:.3f}',f'{f_b:.3f}',f'{f_c:.3f}'])
        
        # Check if the above found point is root
        if func(c) == 0.0:
            break
        
        # Decide the side to repeat the steps
        elif func(c) * func(a) < 0:
            b = c
        else:
            a = c
    return table_data,c

# Driver code to test above function
# Initial values assumed
table_data,root = regulaFalsi(a, b)
print("root =",root)

print(tabulate(table_data,headers=["iteration","a",'b','c','f(a)','f(b)','f(c)'],tablefmt="pretty"))

#ploting
x = np.linspace(-3,3)
plt.plot(x,func(x),label='y=func(x)')
plt.scatter(root,func(root),color='r',label='root')
plt.axhline(0,label='y=0')
plt.axvline(root,label='x=root')
plt.grid()
plt.title("falsi method")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.legend()
plt.show()