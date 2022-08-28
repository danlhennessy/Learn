fn main() {
    let mut x = 4; let y = 5; // Default integer type is i32
    println!("x y is: {} {}", x, y);

    {
        let x: i16 = 2;  // Specifying x to have the data type i16
        println!("x is: {}", x);
    }

    x = x + 1;
    println!("x is: {}", x);

    const SECONDS_IN_MINUTE: u32 = 60; // u32 is an unsigned 32 bit integer (Min 0, Max (2^32 - 1))
    println!("{}", SECONDS_IN_MINUTE);

}