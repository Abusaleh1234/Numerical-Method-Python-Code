import math
import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate

table_data = []

def f(x):
    return 2*x*x-4*x+1

def g(x):
    return 0.5*x*x+0.25

def gprime(x):
    return x

lower = float(input("lower=:"))
upper = float(input("upper=:"))

if f(lower)*f(upper) >=0:
    print("there is no root in this range")
    exit()

val = float(input("arbitrary value for gprime:"))

if gprime(val) >=1:
    print('the values gives %.3f which is >=1, try another value to satisfy condition' %gprime(val))
    exit()


x0 = (lower+upper)/2.0
Root=[x0]

def fixedpositionIteration(root):
    n=1
    flag =1
    while flag == 1:
        table_data.append([n,f'{root:.10f}'])
        NewRoot=g(root)
        Root.append(NewRoot)
        if abs(NewRoot-root) <= 1e-10: flag=0
        root = NewRoot
        n+=1

    return root

root = fixedpositionIteration(x0)
print(f'root = {root}\n')


print(tabulate(table_data,headers=["StepNo","Root/f(x)"],tablefmt='pretty'))

x = np.linspace(lower,upper,100)
y = g(x)
plt.plot(x,y)
plt.scatter(root,g(root),color = 'r')
plt.axhline(root,lw=0.5,color='green')
plt.axvline(root,lw=0.5,color='purple')
plt.grid()
plt.show()