# Importing NumPy Library
import numpy as np
import sys

n = int(input())
temp = []

for i in range(n):
    a=[]
    for j in range(n+1):
        a.append(float(input()))
    temp.append(a)

A = np.array(temp)

# Applying Gauss Jordan Elimination
for i in range(n):
    if A[i][i] == 0.0:
        sys.exit('Divide by zero detected!')
    for j in range(n):
        if i != j:
            ratio = A[j][i] / A[i][i]
            for k in range(n + 1):
                A[j][k] = A[j][k] - ratio * A[i][k]

print(A,end='\n')

# Obtaining Solution
x = np.zeros(n)
for i in range(n):
    x[i] = A[i][n] / A[i][i]

# Displaying solution
print('\nRequired solution is: ')
for i in range(n):
    print('X%d = %0.2f' % (i, x[i]), end='\t')