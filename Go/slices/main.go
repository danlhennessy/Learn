package main

import "fmt"

func main() {
	var myslice []int

	for i := 7; i < 21; i++ {
		myslice = append(myslice, i)
	}

	fmt.Println(myslice)
	fmt.Println(myslice[7:12])
}
