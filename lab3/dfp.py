import numpy as np
from numpy.linalg import norm
import math


def f(x: np.ndarray) -> float:
    x1, x2 = x[0], x[1]
    return x1 ** 2 + 4 * x2 ** 2 + x1 * x2 + x1


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


def dfp(x: np.ndarray, e1: float, e2: float, m: int) -> np.ndarray:
    a = np.eye(len(x))
    a_prev = a.copy()
    prev = False

    grad_prev = np.zeros(2)
    x_prev = np.zeros(2)
    
    for k in range(m):
        grad = gradient(x)
        if norm(grad) <= e1:
            return x
        
        if k >= 1:
            delta_g = grad - grad_prev
            delta_x = x - x_prev
            
            term1 = np.outer(delta_x, delta_x) / np.dot(delta_x, delta_g)
            
            a_prev_dg = a_prev @ delta_g
            term2 = np.outer(a_prev_dg, a_prev_dg) / np.dot(delta_g, a_prev_dg)
            
            a = a_prev + term1 - term2
        
        d = -a @ grad
        t = gold(lambda t: f(x + t * d), -100.0, 100.0, 1e-6)
        
        y = x + t * d
        fx = f(x)
        fy = f(y)

        if all([prev, norm(y - x) < e2, abs(fy - fx) < e2]):
            return y
        prev = norm(y - x) < e2 and abs(fy - fx) < e2
        
        x_prev = x.copy()
        grad_prev = grad.copy()
        a_prev = a.copy()
        x = y
    return x


if __name__ == "__main__":
    x = dfp(np.array([3.0, 1.0]), 0.1, 0.15, 100)
    print(f"x*={x}, f(x*)={f(x)}")
