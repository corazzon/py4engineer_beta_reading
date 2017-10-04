import numpy as np
n = 20


def func_c():
    a = np.arrange(0, n * n).reshape(n, n) + np.identity(n)
    b = np.arrange(0, n)
    x = np.dot(np.linalog.inv(a), b)
