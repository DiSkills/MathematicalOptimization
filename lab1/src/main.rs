mod dichotomy;
mod golden_ratio;

fn f(x: f64) -> f64 {
    return x * x + 2.0;
}

fn main() {
    let mut x: f64;

    x = dichotomy::search_min(f, 0.5, 1.0, -3.0, 7.0);
    println!("dichotomy: x = {}, f(x) = {}", x, f(x));

    x = golden_ratio::search_min(f, 0.2, -3.0, 7.0);
    println!("golden ration: x = {}, f(x) = {}", x, f(x));
}
