import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

def f(XX):
    y = []
    for x in XX:
        if x < 0.5 and x > -0.5:
            y.append(1 - 2 * abs(x))
        else:
            y.append(0)
    return y

X = [-1, -0.5, 0, 0.5, 1]
Y = f(X)

condition_3 = CubicSpline(X, Y, bc_type = "natural")
condition_4 = CubicSpline(X, Y, bc_type = "clamped")

x_new = np.linspace(-1, 1, 1000)
y_f = f(x_new)
y_3 = condition_3(x_new)
y_4 = condition_4(x_new)

plt.plot(x_new, y_f, label = "f(x)")
plt.plot(x_new, y_3, label = "Condition 3")
plt.plot(x_new, y_4, label = "Condition 4")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()