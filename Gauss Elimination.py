import numpy as np

temp = []

r = int(input())
c = int(input())

for i in range(r):
    a=[]
    for j in range(c):
        a.append(float(input()))
    temp.append(a)

A = np.array(temp)
# print('\n',A,end='\n')

#Forward Elimination
for i in range(r):
    if A[i][i] == 0.0 : print("Divide by Zero detected"); exit()
    for j in range(i+1,r):
        ratio = A[j][i] / A[i][i]
        for k in range(c):
            A[j][k] = A[j][k] - ratio*A[i][k]

print(A,end='\n')

#Backward Substitution
X = np.zeros(r)
X[r - 1] = A[r - 1][c - 1] / A[r - 1][c - 2]

for i in range(r-2,-1,-1):
    X[i] =  A[i][c - 1]
    for j in range(i+1,r):
        X[i] = X[i] - A[i][j] * X[j]
    X[i] = X[i] / A[i][i]

#for output
for i in range(r):
    print('x%d = %.2f' % (i, X[i]), end='\n')