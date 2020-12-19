def part1(ipt, x, y):
    pos = (0, 0)

    count = 0
    while pos[1] < len(ipt):
        pos = ((pos[0] + x) % (len(ipt[0]) - 1), pos[1] + y)

        if pos[1] >= len(ipt):
            break

        if ipt[pos[1]][pos[0]] == '#':
            count += 1

    return count


def part2(ipt):
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    total = 1
    for s in slopes:
        total *= part1(ipt, *s)

    return total


if __name__ == '__main__':
    with open('input.txt') as fp:
        ipt = [l for l in fp]
        print(part1(ipt, 3, 1))
        print(part2(ipt))
