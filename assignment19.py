import numpy as np
import math

#       QUESTION 1

# a = np.random.random((10, 1))  # Alternative: np.random.rand(10, 1)
# print(np.mean(a))
#
#
# #       QUESTION 2
#
# a = np.random.rand(20, 1)
# print(np.var(a))
# print(np.std(a))
#
#
# #       QUESTION 3
#
# A = np.random.random((10, 20))
# B = np.random.random((20, 25))
# print(np.matmul(A, B))
# print(np.sum(np.matmul(A, B)))


#       QUESTION 4

A = np.random.random((10, 1))


def func(x):
    return 1/(1 + math.exp(-x))


NewFunc = np.vectorize(func)
print(NewFunc(A))
