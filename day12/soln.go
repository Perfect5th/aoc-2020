package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
)

type inst struct {
	dir rune
	val int
}

type floatInst struct {
	dir rune
	val float64
}

func parseFloat(ipt []string) (parsed []floatInst) {
	parsed = make([]floatInst, len(ipt))
	for _, i := range ipt {
		asRunes := []rune(i)
		val, _ := strconv.ParseFloat(i[1:], 64)
		parsed = append(parsed, floatInst{asRunes[0], val})
	}
	return
}

func parse(ipt []string) (parsed []inst) {
	parsed = make([]inst, len(ipt))
	for _, i := range ipt {
		asRunes := []rune(i)
		val, _ := strconv.Atoi(i[1:])
		parsed = append(parsed, inst{asRunes[0], val})
	}
	return
}

func solve(ipt []string) {
	parsed := parseFloat(ipt)
	position := []float64{0, 0, 90}
	
	for _, i := range parsed {
		d := i.dir
		v := i.val

		switch (d) {
		case 'N':
			position[0] += v
			break
		case 'E':
			position[1] += v
			break
		case 'S':
			position[0] -= v
			break
		case 'W':
			position[1] -= v
			break
		case 'L':
			position[2] -= v
			break
		case 'R':
			position[2] += v
			break
		case 'F':
			rads := position[2] * math.Pi / 180
			x := math.Cos(rads) * v
			y := math.Sin(rads) * v
			position[0] += x
			position[1] += y
		}
	}

	fmt.Println(math.Round(math.Abs(position[0]) + math.Abs(position[1])))
}

func solve2(ipt []string) {
	parsed := parse(ipt)
	position := []int{1, 10}
	ship := []float64{0, 0}

	for _, i := range parsed {
		d := i.dir
		v := i.val

		switch (d) {
		case 'N':
			position[0] += v
			break
		case 'E':
			position[1] += v
			break
		case 'S':
			position[0] -= v
			break
		case 'W':
			position[1] -= v
			break
		case 'L':
			for i := 0; i < v / 90; i++ {
				n := position[0]
				position[0] = position[1]
				position[1] = -n
			}
			break
		case 'R':
			for i := 0; i < v / 90; i++ {
				n := position[0]
				position[0] = -position[1]
				position[1] = n
			}
			break
		case 'F':
			ship[0] += float64(position[0] * v)
			ship[1] += float64(position[1] * v)
		}
	}

	fmt.Println(math.Abs(ship[0]) + math.Abs(ship[1]))
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
	solve2(ipt)
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
	solve2(ipt)
	fmt.Println("")
}