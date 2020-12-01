package main

import (
	"bufio"
	"errors"
	"fmt"
	"log"
	"os"
	"strconv"
)

func main() {
	var numbers []int

	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		number, err := strconv.Atoi(scanner.Text())
		if err != nil {
			log.Fatal(err)
		}

		numbers = append(numbers, number)
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	soln1, err1 := part1(numbers)
	soln2, err2 := part2(numbers)

	if err1 != nil {
		fmt.Println("Issue with 1st soln", err1)
	} else {
		fmt.Println("Part 1:", soln1)
	}

	if err2 != nil {
		fmt.Println("Issue with 2nd soln", err2)
	} else {
		fmt.Println("Part 2:", soln2)
	}
}

func part1(ipt []int) (int, error) {
	// BRUTE FORCE BECAUSE WHY NOT
	for i, n := range ipt {
		for j, m := range ipt {
			if i == j {
				continue
			}

			if n+m == 2020 {
				return n * m, nil
			}
		}
	}

	return 0, errors.New("Unable to find numbers that fulfilled constraint")
}

func part2(ipt []int) (int, error) {
	// BRUTE FORCE BECAUSE WHY NOT
	for i, n := range ipt {
		for j, m := range ipt {
			for k, e := range ipt {
				if i == j || i == k || j == k {
					continue
				}

				if n+m+e == 2020 {
					return n * m * e, nil
				}
			}
		}
	}

	return 0, errors.New("Unable to find numbers that fulfilled constraint")
}
