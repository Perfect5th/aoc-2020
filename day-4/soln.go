package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

var fields = []string{"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

func readPassport(ipt []string, ch chan string) {
	var passport strings.Builder
	for _, l := range ipt {
		if l == "" {
			ch <- passport.String()
			passport.Reset()
			continue
		}

		passport.WriteString(l)
	}

	ch <- passport.String()
	close(ch)
}

func part1(ipt []string) (valid int) {
	passports := make(chan string)
	go readPassport(ipt, passports)

	for passport := range passports {
		isValid := true

		for _, f := range fields {
			if !strings.Contains(passport, f) {
				isValid = false
				break
			}
		}

		if isValid {
			valid++
		}
	}
	return
}

func part2(ipt []string) (valid int) {
	return
}

func main() {
	var ipt []string

	file, _ := os.Open("input.txt")
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