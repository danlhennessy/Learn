fn main() {
    let mut x = 4;
    println!("x is: {}", x);

    {
        let x = 2;
        println!("x is: {}", x);
    }

    x = x + 1;
    println!("x is: {}", x);

    const SECONDS_IN_MINUTE: u32 = 60; // u32 is an unsigned 32 bit integer (Min 0, Max 4294967295)
    println!("{}", SECONDS_IN_MINUTE);

}