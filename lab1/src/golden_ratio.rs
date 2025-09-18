pub fn search_min(
    f: fn(f64) -> f64,
    delta: f64,
    mut a: f64,
    mut b: f64,
) -> f64
{
    let mut y: f64 = a + (3.0 - f64::sqrt(5.0)) / 2.0 * (b - a);
    let mut z: f64 = a + b - y;

    while b - a >= delta {
        let fy: f64 = f(y);
        let fz: f64 = f(z);
        if fy <= fz {
            b = z;
            z = y;
            y = a + b - y;
        } else {
            a = y;
            y = z;
            z = a + b - z;
        }
    }
    return (a + b) / 2.0;
}
