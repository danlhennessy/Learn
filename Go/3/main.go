package main

import "fmt"

func main() {
	var pole int = 3
	pole += 2
	fmt.Printf("val: %v\n", pole)
	fmt.Printf("type: %T\n", pole)

	var point *int
	point = &pole
	fmt.Println(point)
}
