import numpy as np

def f(x, y):
    return np.sin(x) + y

h = 0.01
Y = 2
X = 0

for i in range(10):
    Y = Y + (h / 2) * (f(X, Y) + f(X + h, Y + h * f(X, Y)))
    X = X + h

print(Y)

for i in range(40):
    Y = Y + (h / 2) * (f(X, Y) + f(X + h, Y + h * f(X, Y)))
    X = X + h

print(Y)