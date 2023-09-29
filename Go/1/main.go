package main

import "fmt"

func main() {
	for j := 7; j <= 25; j++ {
		k := j
		j += 1
		fmt.Println(k, j)
	}
}
