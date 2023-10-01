package main

import "fmt"

func main() {
	var pole int = 3
	pole += 2
	fmt.Printf("val: %v\n", pole)
	fmt.Printf("type: %T\n", pole)

	point := &pole
	fmt.Println(point)
	pole += 2
	fmt.Println(pole)
	fmt.Println(point)
	fmt.Println(*point)
	*point = 21
	fmt.Println(pole)
	fmt.Println(*point)

}
