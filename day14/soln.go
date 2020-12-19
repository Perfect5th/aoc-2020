package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func solve(ipt []string) {
	var buses []int

	strBuses := strings.Split(ipt[1], ",")
	start, _ := strconv.Atoi(ipt[0])
	times := make(map[int]int)

	for _, i := range strBuses {
		if i != "x" {
			asInt, _ := strconv.Atoi(i)
			buses = append(buses, asInt)
		}
	}

	for earliest := start; len(times) < len(buses); earliest++ {
		for _, bus := range buses {
			if earliest % bus == 0 {
				times[earliest] = bus
			}
		}
	}

	answerKey := 0
	for k := range times {
		if answerKey == 0 || k < answerKey {
			answerKey = k
		}
	}

	fmt.Println((answerKey - start) * times[answerKey])

	start = buses[0]
	increment := start
	for i := 1; i < len(strBuses); {
		if strBuses[i] == "x" {
			i++
			continue
		}

		b, _ := strconv.Atoi(strBuses[i])
		if (start + i) % b == 0 {
			increment *= b
			i++
			continue
		}

		start += increment
	}

	fmt.Println(start)
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
	solve(ipt)
	fmt.Println("")

	ipt = nil
	real, _ := os.Open("input.txt")
	defer real.Close()

	scanner = bufio.NewScanner(real)
	for scanner.Scan() {
		ipt = append(ipt, scanner.Text())
	}

	fmt.Println("RESULT")
	solve(ipt)
	fmt.Println("")
}