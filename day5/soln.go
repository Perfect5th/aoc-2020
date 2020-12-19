package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

var binMap = map[string]string{
	"F": "0",
	"B": "1",
	"L": "0",
	"R": "1",
}

func toBinary(ticket string) (asBinary uint64) {
	for old, new := range binMap {
		ticket = strings.Replace(ticket, old, new, -1)
	}

	asBinary, err := strconv.ParseUint(ticket, 2, 64)
	if err != nil {
		log.Fatal(err)
	}

	return
}

func part1(ipt []string) (max uint64) {
	for _, ticket := range ipt {
		asBinary := toBinary(ticket)
		if asBinary > max {
			max = asBinary
		}
	}

	return
}

func part2(ipt []string) uint64 {
	for i := 1; i < len(ipt) - 1; i++ {
		prev := toBinary(ipt[i-1])
		curr := toBinary(ipt[i])
		next := toBinary(ipt[i+1])

		if prev != curr - 1 && next != curr + 1 {
			return curr
		}
	}

	return 0
}

func main() {
	var ipt []string

	file, _ := os.Open("input.txt")
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		ipt = append(ipt, scanner.Text())
	}

	fmt.Println(part1(ipt))
	fmt.Println(part2(ipt))
}