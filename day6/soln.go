package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func buildAlphabet() []rune {
	var qs []rune

	for i := 'a'; i < 'a' + 26; i++ {
		qs = append(qs, i)
	}

	return qs
}

func readCard(ipt []string, ch chan string) {
	var card strings.Builder
	for _, l := range ipt {
		if l == "" {
			ch <- card.String()
			card.Reset()
			continue
		}

		if strings.HasPrefix(l, " ") {
			card.WriteString(l)
		} else {
			card.WriteString(" ")
			card.WriteString(l)
		}
	}

		ch <- card.String()
		close(ch)
}

func part1(ipt []string) (total int) {
	cards := make(chan string)
	alpha := buildAlphabet()
	go readCard(ipt, cards)

	for card := range cards {
		answered := 0

		for _, q := range alpha {
			if strings.ContainsRune(card, q) {
				answered++
			}
		}

		total += answered
	}

	return
}

func part2(ipt []string) (total int) {
	cards := make(chan string)
	go readCard(ipt, cards)

	for card := range cards {
		answered := 0
		counts := make(map[rune]int)
		res := strings.Split(card, " ")

		for _, r := range res {
			for _, q := range r {
				counts[q]++
			}
		}

		for _, v := range counts {
			if v == len(res) - 1 {
				answered++
			}
		}

		total += answered
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

	fmt.Println(part1(ipt))
	fmt.Println(part2(ipt))
}