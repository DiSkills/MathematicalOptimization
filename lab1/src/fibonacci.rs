pub fn search_min(
    f: fn(f64) -> f64,
    delta: f64,
    eps: f64,
    mut a: f64,
    mut b: f64,
) -> f64
{
    let mut f1: i32 = 1;
    let mut f2: i32 = 1;
    let mut n: i32 = 1;
    while f64::from(f2) < (b - a) / delta {
        let tmp: i32 = f1 + f2;
        f1 = f2;
        f2 = tmp;
        n += 1;
    }

    let mut y: f64 = a + f64::from(f1) / f64::from(f2) * (b - a);
    let mut x: f64 = a + b - y;

    while n > 2 {
        let fx: f64 = f(x);
        let fy: f64 = f(y);
        if fx < fy {
            b = y;
            y = x;
            x = a + b - y;
        } else {
            a = x;
            x = y;
            y = a + b - x;
        }
        n -= 1;
    }

    y += eps;
    if f(x) < f(y) {
        b = y;
    } else {
        a = x;
    }
    return (a + b) / 2.0;
}
