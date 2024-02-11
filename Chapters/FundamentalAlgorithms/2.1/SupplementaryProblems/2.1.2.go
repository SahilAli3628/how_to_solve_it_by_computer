package main

import "fmt"

func main() {
	var a, b, c, t1, t2 int
	fmt.Println("Enter 3 numbers a, b, c")
	fmt.Scanf("%d", &a)
	fmt.Scanf("%d", &b)
	fmt.Scanf("%d", &c)
	fmt.Printf("\nBefore Swapping: a = %d, b = %d, c = %d\n", a, b, c)
	fmt.Println("Swapping: a -> b, b -> c, c -> a")
	t1 = b
	t2 = c
	b = a
	c = t1
	a = t2
	fmt.Printf("\nAfter Swapping: a = %d, b = %d, c = %d\n", a, b, c)


}
