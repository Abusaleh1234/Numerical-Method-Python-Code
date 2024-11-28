import numpy as np
import matplotlib.pyplot as plt
import math

def func(x):
    return math.exp(-x)-x

def derivFunc(x):
    return -1*math.exp(-x)-1


def NewtonRapson(root):
    n  = 1
    flag = 1
    while flag==1:
        if derivFunc(root) == 0.0 : break
        NewRoot = root - (func(root) / derivFunc(root))
        Root.append(NewRoot)
        print("step = %d" %n, "root= %.5f" %root , "NewRoot%d= %.5f" %(n,NewRoot) )
        if NewRoot -root <= 1e-10: flag= 0; break
        n+=1
        root = NewRoot
    return root

# Driver program to test above
x0 = int(input("take initial value= "))
Root = [x0]
root = NewtonRapson(x0)
print("The value of the root is : ","%.4f" % root)


plt.plot(Root,marker='o')
plt.show()
