package main

import (
	"fmt"
	"math/rand"
)

func main() {

	var x = []int{}

	for i := 1; i <= 100; i++ {
		x = append(x, rand.Intn(100))
	}

	fmt.Println(x)
}
