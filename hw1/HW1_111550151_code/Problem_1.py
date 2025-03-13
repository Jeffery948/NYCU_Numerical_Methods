import numpy as np

def f(x):
    return x * np.sin((x - 2) / (x - 1))

def bisection(a, b):
    tol = 1e-5
    num_iter = 0
    root = 0
    if f(a) * f(b) > 0:
        return "No root or bisection fails", num_iter
    while abs(a - b) > tol:
        m = (a + b) / 2
        root = m
        if f(a) * f(m) < 0:
            b = m
        else:
            a = m
        num_iter += 1
        if f(m) == 0 or num_iter >= 1e5:
            break

    return root, num_iter

for i in range(19):
    r, num_iter = bisection(0.9 + i * 0.005, 0.9 + i * 0.005 + 0.005)
    #print(0.9 + i * 0.005, 0.9 + i * 0.005 + 0.005)
    print(r, num_iter)