#[macro_use]
extern crate fstrings;

fn main() {
    let name = "Dan"; let age = 29;

    println_f!("Hello, {name}, age: {age}!");
}
