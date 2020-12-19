package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func solve(ipt string, target int) {
	var iptInts []int

	ipts := strings.Split(ipt, ",")

	for _, i := range ipts {
		asInt, _ := strconv.Atoi(i)
		iptInts = append(iptInts, asInt)
	}

	seen := make(map[int][]int)
	for i, v := range iptInts {
		seen[v] = append(seen[v], i+1)
	}

	last := iptInts[len(iptInts)-1]
	for i := len(iptInts) + 1; i < target+1; i++ {
		curr := 0

		if len(seen[last]) != 1 {
			curr = seen[last][len(seen[last])-1] - seen[last][len(seen[last])-2]
		}

		seen[curr] = append(seen[curr], i)

		last = curr
	}

	fmt.Println(last)
}

func main() {
	var ipt []string
	test, _ := os.Open("test_input.txt")
	defer test.Close()

	scanner := bufio.NewScanner(test)
	for scanner.Scan() {
		ipt = append(ipt, scanner.Text())
	}

	fmt.Println("TEST")
	solve(ipt[0], 10)
	fmt.Println("")

	ipt = nil
	real, _ := os.Open("input.txt")
	defer real.Close()

	scanner = bufio.NewScanner(real)
	for scanner.Scan() {
		ipt = append(ipt, scanner.Text())
	}

	fmt.Println("RESULT")
	solve(ipt[0], 2020)
	solve(ipt[0], 30000000)
	fmt.Println("")
}
