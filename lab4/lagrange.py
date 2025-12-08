import numpy as np

from powell import powell


def f(x: np.ndarray) -> float:
    x1, x2 = x[0], x[1]
    return x1 ** 2 + 4 * x2 ** 2 + x1 * x2 + x1


def p(x: np.ndarray, r: float, l: float) -> float:
    x1, x2 = x[0], x[1]
    return l * (x1 + x2 - 2) + r / 2 * (x1 + x2 - 2) ** 2


def lagrange(x: np.ndarray, l: float, r: float, c: float, eps: float) -> np.ndarray:
    while True:
        y = powell(lambda x: f(x) + p(x, r, l), x, 0.01, 100)
        if abs(p(y, r, l)) <= eps:
            return y
        l += r * (y[0] + y[1] - 2)
        r *= c
        x = y


if __name__ == "__main__":
    x = lagrange(np.array([3.0, 1.0]), 0.0, 1.0, 10.0, 0.01)
    print(f"x*={x}, f(x*)={f(x)}")
