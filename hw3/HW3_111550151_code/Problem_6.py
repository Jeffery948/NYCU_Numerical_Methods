import numpy as np

def power(x):
    return 1 - (x ** 2) / 2 + (x ** 4) / 24

def chebyshev(x):
    return 1.0059 - 0.5114 * (x ** 2) + 0.04 * (x ** 4)

X = [-1, -0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1]

print("X\tChebyshev error\t\tpower error")

for x in X:
    error1 = abs(np.cos(x) - chebyshev(x))
    error2 = abs(np.cos(x) - power(x))
    print("{}\t{}\t{}\t".format(x, error1, error2))