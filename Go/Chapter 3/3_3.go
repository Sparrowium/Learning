package main

import "fmt"

func main() {

	type Employee struct {
		firstName string
		lastName  string
		id        int
	}

	var a = Employee{
		firstName: "Jac",
		lastName:  "Kie",
		id:        45,
	}

	fmt.Println(a)
}
