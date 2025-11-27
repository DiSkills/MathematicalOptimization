import math

import numpy as np

from numpy.linalg import norm, matrix_rank


def f(x: np.ndarray) -> float:
    x1, x2 = x[0], x[1]
    return x1 ** 2 + 4 * x2 ** 2 + x1 * x2 + x1


def gold(func, a: float, b: float, delta: float) -> float:
    y = a + ((3 - math.sqrt(5)) / 2) * (b - a)
    z = a + b - y
    while b - a > delta:
        fy, fz = func(y), func(z)
        if fy <= fz:
            b = z
            z = y
            y = a + b - y
        else:
            a = y
            y = z
            z = a + b - z
    return (a + b) / 2


def powell(x: np.ndarray, eps: float, m: int) -> np.ndarray:
    n = len(x)
    D = [np.eye(n)[i] for i in range(n)]
    d0 = D[-1].copy()
    while m > 0:
        y = [x.copy()]
        for i in range(n):
            d = d0 if i == 0 else D[i - 1]
            t = gold(lambda t: f(y[i] + t * d), -100, 100, 1e-6)

            y.append(y[i] + t * d)
            if i == n - 1 and norm(y[n] - y[0]) < eps:
                return y[n]

        t = gold(lambda t: f(y[n] + t * d0), -100, 100, 1e-6)
        y.append(y[n] + t * d0)
        if norm(y[n + 1] - y[1]) < eps:
            return y[n + 1]
        z = y[n + 1]
        if norm(z - x) < eps:
            return z
        d = y[n + 1] - y[1]

        D_new = D[1:] + [d]
        if matrix_rank(np.column_stack(D_new)) == n:
            D = D_new
            d0 = d
        x = z

        m -= 1
    return x


if __name__ == "__main__":
    x = powell(np.array([3.0, 1.0]), 0.1, 100)
    print(f"x*={x}, f(x*)={f(x)}")
