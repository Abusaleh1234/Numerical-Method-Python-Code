import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
    Y = 0.5*(x+y)
    return Y

x_values =[]
y_values =[]
sz = int(input("total size = "))

#input section
for i in range(sz):
    x = float(input())
    x_values.append(x)

for i in range(sz):
    x= float(input())
    y_values.append(x)


y1 = f(x_values[1],y_values[1])
y2 = f(x_values[2],y_values[2])
y3 = f(x_values[3],y_values[3])


#predictor formula
n = 3
h = x_values[1] - x_values[0]

y4p = y_values[0] + (4*h)/3 * (2*y1-y2+2*y3)

#correcting formula
y4 = f(2,y4p)
y4c = y_values[2] + (h/3)*(y2+4*y3+y4)

print(f"\ny4p={y4p:.3f}\ny4c ={y4p:.4f}")

# Plotting the results
x_values.append(2)
y_values.append(y4c)

plt.plot(x_values,y_values,label='predicted line',marker='o')
plt.title("Mines Method")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()


