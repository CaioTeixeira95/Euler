use std::thread;

const MAX_VALUE: i64 = 2_000_000;
const THREADS: i64 = 50;

fn is_prime(n: i64) -> bool {

    if n == 2 {
        return true;
    }

    if n < 2 || n % 2 == 0 {
        return false;
    }

    for i in (3..=((n as f64).sqrt() as i64)).step_by(2) {
        if n % i == 0 {
            return false;
        }
    }
    true
}

fn calculate(mut from: i64, to: i64) -> i64 {
    let mut total: i64 = 0;
    while from <= to {
        if is_prime(from) {
            total += from;
        }
        from += 1;
    }
    total
}

fn main() {
    let mut childrens = vec![];
    let size = MAX_VALUE / THREADS;
    let mut actual = 1;
    for _ in 0..THREADS {
        childrens.push(thread::spawn(move || {
            println!("Calculating from {} to {}", actual, (actual + size) - 1);
            calculate(actual, (actual + size) - 1)
        }));
        actual += size;
    }
    let total: i64 = childrens
        .into_iter()
        .map(|child| child.join().unwrap())
        .sum();

    println!("Total: {}", total);
}
