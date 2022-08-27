fn main() {
    let mut tup: (i32, bool, char) = (1, true, 's');  // (i32, bool, char) = this tuples type
    println!("{}", tup.0);  // print element in index 0 of tup

    tup.0 = 10;
    println!("{}", tup.0);
    println!("{}", tup.1);
}
