import numpy as np

def Jacobi_method(old_x):
    new_x = None
    tol = 1e-5
    num_iter = 0
    L = np.array([[0, 0, 0], [2, 0, 0], [-3, 2, 0]])
    D = np.array([[7, 0, 0], [0, 5, 0], [0, 0, 6]])
    U = np.array([[0, -3, 4], [0, 0, 3], [0, 0, 0]])
    b = np.array([6, -5, 2])
    while True:
        num_iter += 1
        new_x = np.linalg.inv(D) @ (b - (L + U) @ old_x)
        if all(abs(new_x - old_x) < tol):
            return new_x, num_iter
        old_x = new_x

ans, number_of_iterations = Jacobi_method([0, 0, 0])
print(ans)
print("Number of iterations : {}".format(number_of_iterations))