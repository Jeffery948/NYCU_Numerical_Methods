import numpy as np

def f(x):
    return x * np.sin((x - 2) / (x - 1))

def secant_method(x0, x1):
    tol = 1e-5
    num_iter = 0
    root = 0
    while abs(x0 - x1) > tol:
        x2 = x1 - f(x1) * ((x0 - x1) / (f(x0) - f(x1)))
        root = x2
        x0 = x1
        x1 = x2
        if abs(f(x0)) < abs(f(x1)):
            tmp = x0
            x0 = x1
            x1 = tmp
        num_iter += 1
        if f(x2) == 0 or num_iter >= 1e5:
            break
    return root, num_iter

for i in range(19):
    r, num_iter = secant_method(0.9 + i * 0.005, 0.9 + i * 0.005 + 0.005)
    #print(0.9 + i * 0.005, 0.9 + i * 0.005 + 0.005)
    print(r, num_iter)