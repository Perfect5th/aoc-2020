def solve1(ipt, print_result=True, x=3, y=1):
    pos = (0, 0)

    count = 0
    while pos[1] < len(ipt):
        pos = ((pos[0] + x) % len(ipt[0]), pos[1] + y)

        if pos[1] >= len(ipt):
            break

        if ipt[pos[1]][pos[0]] == '#':
            count += 1

    if print_result:
        print(count)

    return count


def solve2(ipt):
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    total = 1
    for s in slopes:
        total *= solve1(ipt, False, *s)

    print(total)