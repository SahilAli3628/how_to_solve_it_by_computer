package main

import "fmt"

func main() {
	var a, b int 
	fmt.Println("Enter 2 numbers a and b")
	fmt.Scanf("%d", &a)
	fmt.Scanf("%d", &b)
	fmt.Printf("Before: a = %d, b = %d\n", a, b)
	
	// Method 1
	//a, b = b, a
	
	// Method 2
	/*a = a + b
	b = a - b
	a = a - b
	*/

	// Method 3
	/*
	if a == 0 {
		a = b
		b = 0
	} else if b == 0 {
		b = a
		a = 0
	}
	a = a * b
	b = a / b
	a = a / b
	*/

	// Method 4
	a = a ^ b
	b = a ^ b
	a = a ^ b
	

	fmt.Printf("After: a = %d, b = %d\n", a, b)
}
