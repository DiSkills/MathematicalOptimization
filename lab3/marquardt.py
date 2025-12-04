import numpy as np

from numpy.linalg import inv, norm


def f(x: np.ndarray) -> float:
    x1, x2 = x[0], x[1]
    return x1 ** 2 + 4 * x2 ** 2 + x1 * x2 + x1


def gradient(x: np.ndarray) -> np.ndarray:
    x1, x2 = x[0], x[1]
    return np.array([2.0 * x1 + x2 + 1.0, 8.0 * x2 + x1])


def hessian() -> np.ndarray:
    return np.array([[2, 1], [1, 8]])


def marquardt(x: np.ndarray, e: float, m: int) -> np.ndarray:
    mu = 8 * 10

    for _ in range(m):
        grad = gradient(x)
        if norm(grad) <= e:
            return x
        h = hessian()
        
        h_mu = h + mu * np.eye(2)
        try:
            h_mu_inv = inv(h_mu)
            d = -h_mu_inv @ grad
            
            y = x + d
            if f(y) < f(x):
                x = y
                mu /= 2
            else:
                mu *= 2
        except np.linalg.LinAlgError:
            mu *= 2
    return x


if __name__ == "__main__":
    x = marquardt(np.array([3.0, 1.0]), 0.1, 100)
    print(f"x*={x}, f(x*)={f(x)}")
