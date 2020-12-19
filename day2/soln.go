package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func parse_rule(ipt string) (int, int, string, string) {
	rule_letter_password := strings.Split(ipt, " ")
	rule := rule_letter_password[0]
	letter := rule_letter_password[1]
	password := rule_letter_password[2]

	low_high := strings.Split(rule, "-")
	low := low_high[0]
	high := low_high[1]

	high_int, err := strconv.Atoi(high)
	if err != nil {
		log.Fatal(err)
	}

	low_int, err := strconv.Atoi(low)
	if err != nil {
		log.Fatal(err)
	}

	return low_int, high_int, letter, password
}

func part1(ipt []string) int {
	total := 0
	for _, l := range ipt {
		low, high, letter, password := parse_rule(l)

		count := 0
		for _, char := range password {
			if strings.ContainsRune(letter, char) {
				count++
			}
		}

		if count >= low && count <= high {
			total++
		}
	}

	return total
}

func part2(ipt []string) int {
	total := 0
	for _, l := range ipt {
		low, high, letter, password := parse_rule(l)

		if password[low-1] == letter[0] && password[high-1] == letter[0] {
			continue
		}

		if password[low-1] == letter[0] || password[high-1] == letter[0] {
			total++
		}
	}

	return total
}

func main() {
	var ipt []string

	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		ipt = append(ipt, scanner.Text())
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	fmt.Println(part1(ipt))
	fmt.Println(part2(ipt))
}
