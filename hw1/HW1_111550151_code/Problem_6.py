import numpy as np

def f(x, y):
    return np.array([np.cos(x) ** 2 - y, x ** 2 + y ** 2 - x - 2])

def J(x, y):
    return np.array([[-np.sin(2 * x), -1], [2 * x - 1, 2 * y]])

def newton_method(initial_guess):
    ans = initial_guess
    tol = 1e-6
    num_iter = 0
    while num_iter < 1e5:
        num_iter += 1

        f_val = f(ans[0], ans[1])
        J_val = J(ans[0], ans[1])

        s = np.linalg.solve(J_val, -f_val)

        ans += s

        if np.linalg.norm(s) < tol:
            break

    return ans

ans1 = newton_method([2, 0.2])
print(ans1)
ans2 = newton_method([-0.9, 0.4])
print(ans2)