package main

import (
	"fmt"
	"math"
)

func triangle_numbers(before, n int) int {
	return before + n
}

func factors(n int) int {
	step := 2
	if n%2 == 0 {
		step = 1
	}
	m := map[int]bool{}
	for i := 1; i <= int(math.Sqrt(float64(n))); i += step {
		if n%i == 0 {
			m[i] = true
			m[n/i] = true
		}
	}
	return len(m)
}

func main() {
	var n, before int = 1, 0
	for {
		tn := triangle_numbers(before, n)
		fmt.Println(tn)
		if factors(tn) > 500 {
			fmt.Println("Result:", tn)
			break
		}
		before = tn
		n += 1
	}
}
