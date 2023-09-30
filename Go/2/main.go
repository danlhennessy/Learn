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
	for ind, argument := range myargs {
		fmt.Println("This is the indice:", ind)
		fmt.Println("This is an arg:", argument)
	}
	var nomba int = 12
	var flomba float64 = 13.2

	fmt.Println(int(flomba), float64(nomba))
}
