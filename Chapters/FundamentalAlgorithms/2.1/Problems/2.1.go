package main

import "fmt"

func main() {
	a, b := 721, 463
	var t int
	fmt.Printf("Before swapping, a = %d and b = %d\n", a, b)
	t = a
	a = b
	b = t
	fmt.Printf("After swapping, a = %d and b = %d\n", a, b)

}
