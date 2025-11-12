import math

import numpy as np

from numpy.linalg import norm


def f(x: np.ndarray) -> float:
    x1, x2 = x[0], x[1]
    return x1 * x1 + 4.0 * x2 * x2 + x1 * x2 + x1


def gradient(x: np.ndarray) -> np.ndarray:
    x1, x2 = x[0], x[1]
    return np.array([2.0 * x1 + x2 + 1.0, 8.0 * x2 + x1])


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


def fletcher(x: np.ndarray, eps1: float, eps2: float, m: int) -> np.ndarray:
    d = k = 0
    prev = np.array([0, 0])
    while k <= m:
        grad = gradient(x)
        if norm(grad) <= eps1:
            return x

        if k == 0:
            d = -grad
        else:
            beta = norm(grad) ** 2 / norm(prev) ** 2
            d = -grad + beta * d
        t = gold(lambda t: f(x + t * d), 0, 2, 0.01)

        y = x + t * d
        if norm(y - x) < eps2 and abs(f(y) - f(x)) < eps2:
            return y
        prev = grad.copy()
        x = y
        k += 1
    return x

if __name__ == "__main__":
    x0 = np.array([3, 1], dtype=float)
    x = fletcher(x0, 0.1, 0.15, 10)
    print(f"x* = {x}, f(x*) = {f(x):.6f}")
