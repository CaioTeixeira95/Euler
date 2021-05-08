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

fn main() {
    let mut count: i64 = 6;
    let mut num: i64 = 15;
    loop {
        if is_prime(num) {
            count += 1;
            if count == 10001 {
                println!("{}", num);
                break;
            }
        }
        num += 2;
    }
}