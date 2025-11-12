import math

import numpy as np

from numpy.linalg import inv, norm


def f(x: np.ndarray) -> float:
    x1, x2 = x[0], x[1]
    return x1 * x1 + 4.0 * x2 * x2 + x1 * x2 + x1


def gradient(x: np.ndarray) -> np.ndarray:
    x1, x2 = x[0], x[1]
    return np.array([2.0 * x1 + x2 + 1.0, 8.0 * x2 + x1])


def hessian() -> np.ndarray:
    return np.array([[2, 1], [1, 8]])


def is_positive(matrix: np.ndarray):
    eigenvalues = np.linalg.eigvals(matrix)
    return np.all(eigenvalues > 0)


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


def newton(x: np.ndarray, eps1: float, eps2: float, m: int) -> np.ndarray:
    k = 0
    while k < m:
        grad = gradient(x)
        if norm(grad) <= eps1:
            return x
        h = hessian()
        try:
            h_inv = inv(h)
        except:
            return x
        
        if is_positive(h_inv):
            d = -h_inv @ grad
            t = 1.0
        else:
            d = -grad
            t = gold(lambda t: f(x + t * d), 0, 2, 0.01)
        
        y = x + t * d
        if norm(y - x) < eps2 and abs(f(y) - f(x)) < eps2:
            return y
        x = y
        k += 1
    return x


if __name__ == "__main__":
    x0 = np.array([3, 1], dtype=float)
    x = newton(x0, 0.1, 0.15, 10)
    print(f"x* = {x}, f(x*) = {f(x):.6f}")
