pub fn search_min(
    f: fn(f64) -> f64,
    mut eps: f64,
    delta: f64,
    mut a: f64,
    mut b: f64
) -> f64
{
    eps /= 2.0;

    while b - a >= delta {
        let mid: f64 = (a + b) / 2.0;

        let y: f64 = mid - eps;
        let fy: f64 = f(y);

        let z: f64 = mid + eps;
        let fz: f64 = f(z);

        if fy < fz {
            b = z;
        } else if fy > fz {
            a = y;
        } else {
            a = y;
            b = z;
        }
    }
    return (a + b) / 2.0;
}
