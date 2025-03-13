import numpy as np

def f(x):
    return ((x - 2) ** 3) * ((x - 4) ** 2)

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

    return root

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
    return root

def false_postion(x0, x1):
    tol = 1e-5
    num_iter = 0
    root = 0
    while abs(x0 - x1) > tol:
        x2 = x1 - f(x1) * ((x0 - x1) / (f(x0) - f(x1)))
        root = x2
        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2
        num_iter += 1
        if f(x2) == 0 or num_iter >= 1e5:
            break
    return root

ans = secant_method(2.5, 4.2)
print(ans)
ans1 = bisection(1, 5)
ans2 = secant_method(1, 5)
ans3 = false_postion(1, 5)
print(ans1, ans2, ans3)