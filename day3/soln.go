package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func part1(ipt [][]rune, x int, y int) (count int) {
	posX := 0
	posY := 0

	for posY < len(ipt) {
		posX = (posX + x) % len(ipt[0])
		posY = posY + y

		if posY >= len(ipt) {
			break
		}

		if ipt[posY][posX] == '#' {
			count++
		}
	}

	return
}

func part2(ipt [][]rune) (total int) {
	slopes := [][]int{{1, 1}, {3, 1}, {5, 1}, {7, 1}, {1, 2}}

	total = 1
	for _, s := range slopes {
		total *= part1(ipt, s[0], s[1])
	}

	return
}

func main() {
	var ipt [][]rune

	file, _ := os.Open("input.txt")
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		ipt = append(ipt, []rune(scanner.Text()))
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	fmt.Println(part1(ipt, 3, 1))
	fmt.Println(part2(ipt))
}
