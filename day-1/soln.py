
def part1(ipt, target):
    seen = set()

    for x in ipt:
        if target - x in seen:
            return x * (target - x)

        seen.add(x)

    raise Exception("Couldn't find a match")


def part2(ipt, target):
    for x in ipt:
        try:
            return part1(ipt, 2020 - x) * x
        except:
            continue

    raise Exception("Couldn't find a match")


if __name__ == '__main__':
    ipt = None

    with open('input.txt') as fp:
        ipt = [int(l) for l in fp]
        print(part1(ipt, 2020))
        print(part2(ipt, 2020))