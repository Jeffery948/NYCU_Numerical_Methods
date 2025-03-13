import numpy as np

def Jacobi_method(old_x, test):
    new_x = None
    tol = 1e-5
    num_iter = 0
    max_iter = 1e5
    record = [] # 紀錄收斂過程
    if test == 1 : # 給 (a) and (b)
        L = np.array([[0, 0], [-2, 0]])
        D = np.array([[2, 0], [0, 2]])
        U = np.array([[0, -2], [0, 0]])
        b = np.array([0, 0])
    else: # 給 (c)
        L = np.array([[0, 0], [-1.99, 0]])
        D = np.array([[2, 0], [0, 2]])
        U = np.array([[0, -1.99], [0, 0]])
        b = np.array([0, 0])
    while True:
        num_iter += 1
        new_x = np.linalg.inv(D) @ (b - (L + U) @ old_x)
        record.append(new_x)
        if all(abs(new_x - old_x) < tol) or num_iter == max_iter:
            return new_x, num_iter, record
        old_x = new_x
    
def Gauss_Seidel_method(old_x, test):
    new_x = None
    tol = 1e-5
    num_iter = 0
    max_iter = 1e5
    record = [] # 紀錄收斂過程
    if test == 1 : # 給 (a) and (b)
        L = np.array([[0, 0], [-2, 0]])
        D = np.array([[2, 0], [0, 2]])
        U = np.array([[0, -2], [0, 0]])
        b = np.array([0, 0])
    else: # 給 (c)
        L = np.array([[0, 0], [-1.99, 0]])
        D = np.array([[2, 0], [0, 2]])
        U = np.array([[0, -1.99], [0, 0]])
        b = np.array([0, 0])
    while True:
        num_iter += 1
        new_x = np.linalg.inv(L + D) @ (b - U @ old_x)
        record.append(new_x)
        if all(abs(new_x - old_x) < tol) or num_iter == max_iter:
            return new_x, num_iter, record
        old_x = new_x

ans, number_of_iterations, record = Jacobi_method([1, 1], 1)
print(ans)
print("Number of iterations : {}\n".format(number_of_iterations))
ans, number_of_iterations, record = Jacobi_method([1, -1], 1)
print(ans)
print("Number of iterations : {}".format(number_of_iterations))
print(record[-11:-1])
print("\n")
ans, number_of_iterations, record = Jacobi_method([-1, 1], 1)
print(ans)
print("Number of iterations : {}".format(number_of_iterations))
print(record[-11:-1])
print("\n")
ans, number_of_iterations, record = Jacobi_method([2, 5], 1)
print(ans)
print("Number of iterations : {}".format(number_of_iterations))
print(record[-11:-1])
print("\n")
ans, number_of_iterations, record = Jacobi_method([5, 2], 1)
print(ans)
print("Number of iterations : {}".format(number_of_iterations))
print(record[-11:-1])
print("\n")

ans, number_of_iterations, record = Gauss_Seidel_method([1, 1], 1)
print(ans)
print("Number of iterations : {}\n".format(number_of_iterations))
ans, number_of_iterations, record = Gauss_Seidel_method([1, -1], 1)
print(ans)
print("Number of iterations : {}\n".format(number_of_iterations))
ans, number_of_iterations, record = Gauss_Seidel_method([-1, 1], 1)
print(ans)
print("Number of iterations : {}\n".format(number_of_iterations))
ans, number_of_iterations, record = Gauss_Seidel_method([2, 5], 1)
print(ans)
print("Number of iterations : {}\n".format(number_of_iterations))
ans, number_of_iterations, record = Gauss_Seidel_method([5, 2], 1)
print(ans)
print("Number of iterations : {}\n".format(number_of_iterations))

ans, number_of_iterations, record = Jacobi_method([1, 1], 2)
print(ans)
print("Number of iterations : {}\n".format(number_of_iterations))
ans, number_of_iterations, record = Jacobi_method([1, -1], 2)
print(ans)
print("Number of iterations : {}\n".format(number_of_iterations))
ans, number_of_iterations, record = Jacobi_method([-1, 1], 2)
print(ans)
print("Number of iterations : {}\n".format(number_of_iterations))
ans, number_of_iterations, record = Jacobi_method([2, 5], 2)
print(ans)
print("Number of iterations : {}\n".format(number_of_iterations))
ans, number_of_iterations, record = Jacobi_method([5, 2], 2)
print(ans)
print("Number of iterations : {}\n".format(number_of_iterations))

ans, number_of_iterations, record = Gauss_Seidel_method([1, 1], 2)
print(ans)
print("Number of iterations : {}\n".format(number_of_iterations))
ans, number_of_iterations, record = Gauss_Seidel_method([1, -1], 2)
print(ans)
print("Number of iterations : {}\n".format(number_of_iterations))
ans, number_of_iterations, record = Gauss_Seidel_method([-1, 1], 2)
print(ans)
print("Number of iterations : {}\n".format(number_of_iterations))
ans, number_of_iterations, record = Gauss_Seidel_method([2, 5], 2)
print(ans)
print("Number of iterations : {}\n".format(number_of_iterations))
ans, number_of_iterations, record = Gauss_Seidel_method([5, 2], 2)
print(ans)
print("Number of iterations : {}\n".format(number_of_iterations))