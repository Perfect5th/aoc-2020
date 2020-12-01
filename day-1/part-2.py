#!/bin/env python3

def main(ipt):
    items = [int(l) for l in ipt]
    items.sort()

    for x in range(len(items)):
        for y in range(len(items)):
            for z in range(len(items)):
                if x == y or y == z or x == z:
                    continue

                if items[x] + items[y] + items[z] == 2020:
                    return items[x] * items[y] * items[z]


if __name__ == '__main__':
    with open('input.txt') as ipt:
        print(main(ipt))