import numpy as np

def g1(x):
    return np.sqrt(np.exp(x) / 2)

def g2(x):
    return -np.sqrt(np.exp(x) / 2)

def g3(x):
    return np.log(2 * x * x)

def fixed_point_method1(x):
    tol = 1e-5
    num_iter = 0
    X = g1(x)
    while abs(X - x) > tol:
        x = X
        X = g1(x)
        num_iter += 1
        if num_iter >= 1e5:
            break

    return X

def fixed_point_method2(x):
    tol = 1e-5
    num_iter = 0
    X = g2(x)
    while abs(X - x) > tol:
        x = X
        X = g2(x)
        num_iter += 1
        if num_iter >= 1e5:
            break

    return X

def fixed_point_method3(x):
    tol = 1e-5
    num_iter = 0
    X = g3(x)
    while abs(X - x) > tol:
        x = X
        X = g3(x)
        num_iter += 1
        if num_iter >= 1e5:
            break

    return X

x1, x2 = fixed_point_method1(1.5), fixed_point_method1(-0.5)
print(x1, x2)
x3, x4 = fixed_point_method2(1.5), fixed_point_method2(-0.5)
print(x3, x4)
x5, x6, x7 = fixed_point_method1(2.5), fixed_point_method1(2.6), fixed_point_method1(2.7)
print(x5, x6, x7)
x8, x9, x10 = fixed_point_method2(2.5), fixed_point_method2(2.6), fixed_point_method2(2.7)
print(x8, x9, x10)
x11, x12, x13 = fixed_point_method3(2.5), fixed_point_method3(2.6), fixed_point_method3(2.7)
print(x11, x12, x13)