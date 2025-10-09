use crate::utils::norm;

pub fn descent(
    f: fn((f64, f64)) -> f64,
    gradient: fn((f64, f64)) -> (f64, f64),
    x0: (f64, f64),
    e1: f64,
    e2: f64,
    m: i32,
) -> (f64, f64)
{
    let mut k = 0;
    let mut x = x0;
    loop {
        let g = gradient(x);
        if norm(g) < e1 || k >= m {
            break;
        }

        let t = (g.0 * g.0 + g.1 * g.1) /
            (2.0 * g.0 * g.0 + 2.0 * g.0 * g.1 + 8.0 * g.1 * g.1);
        let y = (x.0 - t * g.0, x.1 - t * g.1);
        if norm((-t * g.0, -t * g.1)) < e2 && f64::abs(f(y) - f(x)) < e2 {
            x = y;
            break;
        }
        x = y;
        k += 1;
    }
    x
}
