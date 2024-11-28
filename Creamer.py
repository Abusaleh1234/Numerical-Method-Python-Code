import numpy as np

r = int(input())
c = int(input())

# Input matrix A
temp1 = []
for i in range(r):
    a = []
    for j in range(c):
        a.append(float(input()))
    temp1.append(a)

A = np.array(temp1)

# Input matrix B (column vector)
temp2 = []
for i in range(r):
    a=[]
    for j in range(1):
        a.append(float(input()))
    temp2.append(a)

B = np.array(temp2)  # Reshape B to a column vector

print("\nMatrix A:")
print(A)
print("\nMatrix B:")
print(B)

# Determinant of A
D = np.linalg.det(A)

if round(D) == 0.000:
    print("Determinant of A is zero. No unique solution exists.")
else:
    print("Determinant of A: %.5f\n" %D)

    # Finding solution for each variable using Cramer's Rule

    for i in range(r):
        C = A.copy()
        C[:, i] = B[:, 0]  # Assign B to the i-th column of C
        Dx = np.linalg.det(C)/D
        print("X",end="")
        print("%d"%i,end=" = ")
        print("%.5f" %Dx)