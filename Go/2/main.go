package main

import (
	"fmt"
	"os"
)

func main() {
	for j := 7; j <= 25; j++ {
		k := j
		j += 1
		fmt.Println(k, j)
	}
	var myargs []string = os.Args
	fmt.Println(myargs)
}
