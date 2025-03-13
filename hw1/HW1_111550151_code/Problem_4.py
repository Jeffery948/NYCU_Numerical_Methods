import numpy as np

def f_1(x):
    return 4 * (x ** 3) - 3 * (x ** 2) + 2 * x - 1

def f_2(x):
    return x ** 2 + np.exp(x) - 5

def muller_method1(x0, x1, x2):
    tol = 1e-5
    num_iter = 0
    while num_iter < 1e5:
        num_iter += 1
        h1 = x1 - x0
        h2 = x0 - x2
        gamma = h2 / h1
        f0 = f_1(x0)
        f1 = f_1(x1)
        f2 = f_1(x2)
        c = f0
        a = (gamma * f1 - f0 * (1 + gamma) + f2) / (gamma * (h1 ** 2) * (1 + gamma))
        b = (f1 - f0 - a * (h1 ** 2)) / h1
        
        if b > 0:
            root = x0 - (2 * c) / (b + np.sqrt((b ** 2) - 4 * a * c))
        else:
            root = x0 - (2 * c) / (b - np.sqrt((b ** 2) - 4 * a * c))

        if root > x0: # rearrange x0, x1, x2, root
            x2 = x0
            if root > x1:
                x0 = x1
                x1 = root
            else:
                x0 = root
        else:
            x1 = x0
            if root > x2:
                x0 = root
            else:
                x0 = x2
                x2 = root

        if abs(f_1(root)) < tol:
            break

        return root
    
def muller_method2(x0, x1, x2):
    tol = 1e-5
    num_iter = 0
    while num_iter < 1e5:
        num_iter += 1
        h1 = x1 - x0
        h2 = x0 - x2
        gamma = h2 / h1
        f0 = f_2(x0)
        f1 = f_2(x1)
        f2 = f_2(x2)
        c = f0
        a = (gamma * f1 - f0 * (1 + gamma) + f2) / (gamma * (h1 ** 2) * (1 + gamma))
        b = (f1 - f0 - a * (h1 ** 2)) / h1
        
        if b > 0:
            root = x0 - (2 * c) / (b + np.sqrt((b ** 2) - 4 * a * c))
        else:
            root = x0 - (2 * c) / (b - np.sqrt((b ** 2) - 4 * a * c))

        if root > x0: # rearrange x0, x1, x2, root
            x2 = x0
            if root > x1:
                x0 = x1
                x1 = root
            else:
                x0 = root
        else:
            x1 = x0
            if root > x2:
                x0 = root
            else:
                x0 = x2
                x2 = root

        if abs(f_2(root)) < tol:
            break

        return root
    
ans1 = muller_method1(0.6, 0.7, 0.5)
print(ans1)
ans2 = muller_method2(1, 1.1, 0.9)
ans3 = muller_method2(-2, -1.9, -2.1)
print(ans2, ans3)