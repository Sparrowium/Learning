package main

import "fmt"

func main() {

	var total int = 0

	for i := 0; i < 10; i++ {
		total := total + i
		fmt.Println(total)
	}

}
