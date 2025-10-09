mod utils;
mod gradient_descent;

fn f(x: (f64, f64)) -> f64 {
    x.0 * x.0 + 4.0 * x.1 * x.1 + x.0 * x.1 + x.0
}

fn gradient(x: (f64, f64)) -> (f64, f64) {
    (2.0 * x.0 + x.1 + 1.0, 8.0 * x.1 + x.0)
}

fn main() {
    let x = gradient_descent::descent(f, gradient, (3.0, 1.0), 0.1, 0.15, 10);
    println!("x = {:?}, f(x) = {}", x, f(x));
}
