package main

import "fmt"

func main() {

	var greetings = [5]string{"Hello", "Hola", "नमस्कार", "こんにちは", "Привіт"}

	x := greetings[:2]
	y := greetings[1:4]
	z := greetings[3:]

	fmt.Println(greetings)
	fmt.Println(x)
	fmt.Println(y)
	fmt.Println(z)

}
