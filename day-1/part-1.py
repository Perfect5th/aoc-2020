#!/bin/env python3

def main(ipt):
    items = [int(l) for l in ipt]
    items.sort()

    for x in range(len(items)):
        for y in range(len(items)):
            if x == y:
                continue

            if items[x] + items[y] == 2020:
                return items[x] * items[y]


if __name__ == '__main__':
    with open('input.txt') as ipt:
        print(main(ipt))