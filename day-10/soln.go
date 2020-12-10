package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

func solve1(ipt []int) {
	sort.Ints(ipt)

	curr := 0
	ones := 0
	threes := 0
	for _, i := range ipt {
		diff := i - curr

		if diff == 3 {
			threes++
		} else if diff == 1 {
			ones++
		}

		curr = i
	}

	threes++
	fmt.Println(threes * ones)
}

func solve2(ipt []int) {
	memo := make([]int, len(ipt))

	for i, v := range ipt[:3] {
		if v <= 3 {
			memo[i]++
		}
	}

	for i, v := range ipt[:len(ipt)-1] {
		var sliceEnd int
		if i + 4 < len(ipt) {
			sliceEnd = i + 4
		} else {
			sliceEnd = len(ipt)
		}

		for j, w := range ipt[i+1:sliceEnd] {
			if j + i + 1 >= len(memo) {
				break
			}

			if w <= v + 3 {
				memo[j+i+1] += memo[i]
			}
		}
	}

	fmt.Println(memo[len(ipt)-1])
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
	solve1(ipt)
	solve2(ipt)
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
	solve1(ipt)
	solve2(ipt)
	fmt.Println("")
}