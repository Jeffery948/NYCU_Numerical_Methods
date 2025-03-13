import numpy as np
import matplotlib.pyplot as plt

def x(u):
    return 3 * u

def y(u):
    return -2.7 * (u ** 3) + 3.3 * (u ** 2) + 0.9 * u

x_point = [0, 1, 2, 3]
y_point = [0, 0.3, 1.7, 1.5]

u_point = np.linspace(0, 1, 1000)

bx = x(u_point)
by = y(u_point)

plt.plot(x_point, y_point, label = "zigzag line")
plt.plot(bx, by, label = "cubic Bezier curve")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()