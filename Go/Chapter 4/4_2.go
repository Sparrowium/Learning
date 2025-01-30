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

	for _, v := range x {
		if v%2 == 0 && v%3 == 0 {
			fmt.Println("Six")
			continue
		}
		if v%2 == 0 {
			fmt.Println("Two")
			continue
		}
		if v%3 == 0 {
			fmt.Println("Three")
			continue
		} else {
			fmt.Println("Never Mind")
		}
	}

}
