import numpy as np
import matplotlib.pyplot as plt

x_d = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
y_d=np.array([0,0.8,0.9,0.1,-0.6,-0.8,-1,-0.9,-0.4])


# n = int(input("Enter size = "))
# x_d=[]
# y_d=[]
# for i in range(n):
#     x = float(input(f"Element {i} = "))
#     x_d.append(x)

# for i in range(n):
#     x = float(input(f"Element{i} = "))
#     y_d.append(x)

# print(f"{x_d}\n{y_d}")

#ploting section
plt.figure(figsize=(12,6))

for i in range(1,7):
    y_est = np.polyfit(x_d, y_d, i)
    plt.subplot(2,3,i)
    plt.plot(x_d, y_d, "o")
    plt.plot(x_d, np.polyval(y_est, x_d))
    plt.title(f"Polynomial order {i}")
    plt.tight_layout()

plt.show()
