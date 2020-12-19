package main

import (
	"bufio"
	"errors"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type prgmResult struct {
	result string
	acc int
}

func runPrgm(ipt []string) prgmResult {
	run := make([]bool, len(ipt))
	pc := 0
	acc := 0

	for !run[pc] && pc < len(ipt) - 1 {
		curr := ipt[pc]
		instVal := strings.Split(curr, " ")
		inst := instVal[0]
		val, _ := strconv.Atoi(instVal[1])
		run[pc] = true

		switch inst {
		case "acc":
			acc += val
			pc++
			break
		case "jmp":
			pc += val
			break
		default:
			pc++
		}
	}

	if pc >= len(ipt) - 1 {
		return prgmResult{"terminated", acc}
	}

	return prgmResult{"looped", acc}
}

func part1(ipt []string) int {
	return runPrgm(ipt).acc
}

func part2(ipt []string) (int, error) {
	for i := 0; i < len(ipt); i++ {
		instVal := strings.Split(ipt[i], " ")
		inst := instVal[0]
		val := instVal[1]
		newIpt := make([]string, len(ipt))
		copy(newIpt, ipt)

		switch (inst) {
		case "jmp":
			newIpt[i] = "nop " + val
			break
		case "nop":
			newIpt[i] = "jmp " + val
			break
		}

		result := runPrgm(newIpt)

		if result.result == "terminated" {
			return result.acc, nil
		}
	}

	return 0, errors.New("couldn't find an answer")
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