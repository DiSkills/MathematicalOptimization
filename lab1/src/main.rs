mod dichotomy;
mod golden_ratio;
mod fibonacci;

fn f(x: f64) -> f64 {
    return x * x + 2.0;
}

fn main() {
    let mut x: f64;

    x = dichotomy::search_min(f, 0.5, 1.0, -3.0, 7.0);
    println!("dichotomy: x = {}, f(x) = {}", x, f(x));

    x = golden_ratio::search_min(f, 0.2, -3.0, 7.0);
    println!("golden ration: x = {}, f(x) = {}", x, f(x));

    x = fibonacci::search_min(f, 1.0, 0.05, -3.0, 7.0);
    println!("fibonacci: x = {}, f(x) = {}", x, f(x));
}
