import numpy as np

from powell import powell


def f(x: np.ndarray) -> float:
    x1, x2 = x[0], x[1]
    return x1 ** 2 + 4 * x2 ** 2 + x1 * x2 + x1


def p(x: np.ndarray, r: float) -> float:
    x1, x2 = x[0], x[1]
    return r / 2 * (x1 + x2 - 2) ** 2


def fines(x: np.ndarray, r: float, c: float, eps: float) -> np.ndarray:
    while True:
        y = powell(lambda x: f(x) + p(x, r), x, 0.01, 100)
        if p(y, r) <= eps:
            return y
        r *= c
        x = y


if __name__ == "__main__":
    x = fines(np.array([3.0, 1.0]), 1.0, 10.0, 0.001)
    print(f"x*={x}, f(x*)={f(x)}")
