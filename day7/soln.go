package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type bags struct {
	count int
	colour string
}

func createGraphmap(ipt []string) map[string][]bags {
	graphmap := make(map[string][]bags)

	for _, i := range ipt {
		var children []bags
		tokens := strings.Split(i, " ")
		parent := strings.Join(tokens[:2], " ")

		if !strings.Contains(i, "no other bags") {
			for i := 4; i < len(tokens); i += 4 {
				num, _ := strconv.Atoi(tokens[i])
				children = append(children, bags{
					num,
					strings.Join(tokens[i+1:i+3], " "),
				})
			}
		}

		graphmap[parent] = children
	}

	return graphmap
}

func part1(ipt []string, target string) (total int) {
	graphmap := createGraphmap(ipt)

	var searchGraph func(string) int
	searchGraph = func(root string) int {
		for _, c := range graphmap[root] {
			if strings.Contains(c.colour, target) || searchGraph(c.colour) > 0 {
				return 1
			}
		}

		return 0
	}

	for k := range graphmap {
		total += searchGraph(k)
	}

	return
}

func part2(ipt []string, target string) int {
	graphmap := createGraphmap(ipt)

	var searchGraph func(string) int
	searchGraph = func(root string) (total int) {
		for _, c := range graphmap[root] {
			total += c.count + c.count * searchGraph(c.colour)
		}

		return
	}

	return searchGraph(target)
}

func main() {
	var ipt []string

	file, _ := os.Open("input.txt")
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		ipt = append(ipt, scanner.Text())
	}

	fmt.Println(part1(ipt, "shiny gold"))
	fmt.Println(part2(ipt, "shiny gold"))
}