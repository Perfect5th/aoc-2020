package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func solve(ipt []int, step int) {
	var invalid int

	for i := step; i < len(ipt); i++ {
		target := ipt[i]
		seen := make(map[int]bool)
		valid := false

		for j := i-step; j < i; j++ {
			candidate := ipt[j]

			if seen[target-candidate] && target != target - candidate {
				valid = true
				break
			} else {
				seen[candidate] = true
			}
		}

		if !valid {
			invalid = target
			fmt.Printf("part 1: %d\n", target)
		}
	}

	for i := 0; i < len(ipt); i++ {
		var ran []int
		total := ipt[i]
		ran = append(ran, ipt[i])

		for j := i+1; j < len(ipt); j++ {
			ran = append(ran, ipt[j])
			total += ipt[j]

			if total == invalid {
				min := 0
				max := 0
				for _, r := range ran {
					if min == 0 || r < min {
						min = r
					} else if r > max {
						max = r
					}
				}

				fmt.Printf("part 2: %d\n", min + max)
				return
			} else if total > invalid {
				break
			}
		}
	}
}

func main() {
	var ipt []int
	test, _ := os.Open("test_input.txt")
	defer test.Close()

	scanner := bufio.NewScanner(test)
	for scanner.Scan() {
		asInt, _ := strconv.Atoi(scanner.Text())
		ipt = append(ipt, asInt)
	}

	fmt.Println("TEST")
	solve(ipt, 5)
	fmt.Println("")

	ipt = nil
	real, _ := os.Open("input.txt")
	defer real.Close()

	scanner = bufio.NewScanner(real)
	for scanner.Scan() {
		asInt, _ := strconv.Atoi(scanner.Text())
		ipt = append(ipt, asInt)
	}

	fmt.Println("RESULT")
	solve(ipt, 25)
	fmt.Println("")
}