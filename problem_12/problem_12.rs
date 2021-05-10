use std::collections::HashMap;


fn triangle_number(before: u32, n: u32) -> u32 {
    before + n
}

fn factors(n: u32) -> u32 {
    let mut step = 2;
    if n % 2 == 0 {
        step = 1;
    }
    let mut facs = HashMap::new();
    for i in (1..((n as f64).sqrt() as u32) + 1).step_by(step) {
        if n % i == 0 {
            facs.insert(i, true);
            facs.insert(n / i, true);
        }
    }
    facs.len() as u32
}

fn main() {
    let mut n: u32 = 1;
    let mut before: u32 = 0;
    loop {
        let tn = triangle_number(before, n);
        println!("{}", tn);
        if factors(tn) > 500 {
            println!("Result: {}", tn);
            break;
        }
        before = tn;
        n += 1;
    }
}
