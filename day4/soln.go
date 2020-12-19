package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
	"strings"
)

var fields = []string{"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
type Rule struct {
	pattern string
	isRange bool
	lower int
	upper int
}
var rules = map[string]Rule {
	"byr": Rule{`(^|\s)byr:(\d{4})($|\s)`, true, 1920, 2002},
	"iyr": Rule{`(^|\s)iyr:(\d{4})($|\s)`, true, 2010, 2020},
	"eyr": Rule{`(^|\s)eyr:(\d{4})($|\s)`, true, 2020, 2030},
	"hgt": Rule{`(^|\s)hgt:(\d+)(cm|in)($|\s)`, false, 0, 0},
	"hcl": Rule{`(^|\s)hcl:#[0-9a-f]{6}($|\s)`, false, 0, 0},
	"ecl": Rule{`(^|\s)ecl:(amb|blu|brn|gry|grn|hzl|oth)($|\s)`, false, 0, 0},
	"pid": Rule{`(^|\s)pid:\d{9}($|\s)`, false, 0, 0},
}

func readPassport(ipt []string, ch chan string) {
	var passport strings.Builder
	for _, l := range ipt {
		if l == "" {
			ch <- passport.String()
			passport.Reset()
			continue
		}

		if strings.HasPrefix(l, " ") {
			passport.WriteString(l)
		} else {
			passport.WriteString(" ")
			passport.WriteString(l)
		}
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

func validate(field string, passport string) bool {
	rule := rules[field]
	expr, _ := regexp.Compile(rule.pattern)
	found := expr.FindStringSubmatch(passport)

	if found == nil {
		return false
	}

	if rule.isRange {
		value, _ := strconv.Atoi(found[2])
		return value >= rule.lower && value <= rule.upper
	}

	if field == "hgt" {
		value, _ := strconv.Atoi(found[2])
		if found[3] == "cm" {
			return value >= 150 && value <= 193
		}

		return value >= 59 && value <= 76
	}

	return true
}

func part2(ipt []string) (valid int) {
	passports := make(chan string)
	go readPassport(ipt, passports)

	for passport := range passports {
		isValid := true

		for _, f := range fields {
			if !validate(f, passport) {
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