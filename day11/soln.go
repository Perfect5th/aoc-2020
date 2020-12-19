package main

import (
	"bufio"
	"errors"
	"fmt"
	"os"
	"strings"
)

type checker func(ipt [][]string, x int, y int) bool
type mover func(x int, y int) (int, int)

func checkAround(ipt [][]string, x int, y int) bool {
	for x1 := x-1; x1 < x+2; x1++ {
		if x1 < 0 || x1 >= len(ipt) {
			continue
		}

		for y1 := y-1; y1 < y+2; y1++ {
			if y1 < 0 || y1 >= len(ipt[0]) {
				continue
			}

			if x1 == x && y1 == y {
				continue
			}

			if ipt[x1][y1] == "#" {
				return false
			}
		}
	}

	return true
}

func countAround(ipt [][]string, x int, y int) (total int) {
	for x1 := x-1; x1 < x+2; x1++ {
		if x1 < 0 || x1 >= len(ipt) {
			continue
		}

		for y1 := y-1; y1 < y+2; y1++ {
			if y1 < 0 || y1 >= len(ipt[0]) {
				continue
			}

			if x1 == x && y1 == y {
				continue
			}

			if ipt[x1][y1] == "#" {
				total++
			}
		}
	}

	return
}

func copyInput(ipt [][]string) [][]string {
	dest := make([][]string, len(ipt))

	for i, row := range ipt {
		dest[i] = make([]string, len(row))
		for j, seat := range row {
			dest[i][j] = seat
		}
	}

	return dest
}

func up(x int, y int) (int, int) { return x - 1, y }
func right(x int, y int) (int, int) { return x, y + 1 }
func down(x int, y int) (int, int) { return x + 1, y }
func left(x int, y int) (int, int) { return x, y - 1 }

var directions = []mover{
	up, right, down, left,
	func (x int, y int) (int, int) { return up(right(x, y)) },
	func (x int, y int) (int, int) { return up(left(x, y)) },
	func (x int, y int) (int, int) { return down(right(x, y)) },
	func (x int, y int) (int, int) { return down(left(x, y)) },
}

type pair struct {
	x int
	y int
}

func moveDir(ipt [][]string, direction mover, x int, y int) (int, int, error) {
	for {
		x, y = direction(x, y)

		if x < 0 || x >= len(ipt) || y < 0 || y >= len(ipt[0]) {
			return -1, -1, errors.New("too far")
		}

		return x, y, nil
	}
}

func countSight(ipt [][]string, x int, y int) (total int) {
	for _, direction := range directions {
		for x1, y1, err := moveDir(ipt, direction, x, y);
			err == nil;
			x1, y1, err = moveDir(ipt, direction, x1, y1) {

			if ipt[x1][y1] == "#" {
				total++
				break
			} else if ipt[x1][y1] == "L" {
				break
			}
		}
	}
	
	return
}

func checkSight(ipt [][]string, x int, y int) bool {
	for _, direction := range directions {
		for x1, y1, err := moveDir(ipt, direction, x, y);
			err == nil;
			x1, y1, err = moveDir(ipt, direction, x1, y1) {
			if ipt[x1][y1] == "#" {
				return false
			} else if ipt[x1][y1] == "L" {
				break
			}
		}
	}	

	return true
}

func solve(ipt [][]string, shouldFill checker, shouldEmpty checker) {
	for {
		nextPhase := copyInput(ipt)

		for x, row := range ipt {
			for y, seat := range row {
				if seat == "L" && shouldFill(ipt, x, y) {
					nextPhase[x][y] = "#"
				} else if seat == "#" && shouldEmpty(ipt, x, y) {
					nextPhase[x][y] = "L"
				}
			}
		}

		changed := false
		for i, row1 := range ipt {
			for j, seat1 := range row1 {
				if seat1 != nextPhase[i][j] {
					changed = true
					break
				}
			}
			if changed {
				break
			}
		}

		if !changed {
			total := 0
			for _, row := range ipt {
				for _, seat := range row {
					if seat == "#" {
						total++
					}
				}
			}
			fmt.Println(total)
			return
		}

		ipt = nextPhase
	}
}

func main() {
	var ipt [][]string
	test, _ := os.Open("test_input.txt")
	defer test.Close()

	scanner := bufio.NewScanner(test)
	for scanner.Scan() {
		ipt = append(ipt, strings.Split(scanner.Text(), ""))
	}

	var part1CountChecker checker = func(ipt [][]string, x int, y int) bool {
		return countAround(ipt, x, y) >= 4
	}

	var part2CountChecker checker = func(ipt [][]string, x int, y int) bool {
		return countSight(ipt, x, y) >= 5
	}

	fmt.Println("TEST")
	solve(ipt, checkAround, part1CountChecker)
	solve(ipt, checkSight, part2CountChecker)
	fmt.Println("")

	ipt = nil
	real, _ := os.Open("input.txt")
	defer real.Close()

	scanner = bufio.NewScanner(real)
	for scanner.Scan() {
		ipt = append(ipt, strings.Split(scanner.Text(), ""))
	}

	fmt.Println("RESULT")
	solve(ipt, checkAround, part1CountChecker)
	solve(ipt, checkSight, part2CountChecker)
	fmt.Println("")
}