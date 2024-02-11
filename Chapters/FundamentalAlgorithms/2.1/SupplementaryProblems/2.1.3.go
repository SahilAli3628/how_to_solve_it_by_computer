package main

import "fmt"

func main() {
	var a, b, c, d, t1, t2, t3 int
	fmt.Println("Enter 4 numbers a, b, c, d")
	fmt.Scanf("%d", &a)
	fmt.Scanf("%d", &b)
	fmt.Scanf("%d", &c)
	fmt.Scanf("%d", &d)
	fmt.Printf("\nBefore Swapping: a = %d, b = %d, c = %d, d =%d\n", a, b, c, d)
	fmt.Println("Swapping: a -> d, d -> c, c -> b, b -> a ")
	t1 = a
	t2 = b
	t3 = c
	c = d
	b = t3
	a = t2
	d = t1
	fmt.Printf("\nAfter Swapping: a = %d, b = %d, c = %d, d = %d\n", a, b, c, d)


}
