import numpy as np

def f(x, y):
    return (x - 1) ** 2 + (y ** 2) / 16

X = np.linspace(-2, 3, 1000000)
Y = np.linspace(-1, 2, 1000000)

ans = 0.0

for i in range(1000000):
    ans += f(X[i], Y[i])

ans = 15 * ans / 1000000
print(ans)