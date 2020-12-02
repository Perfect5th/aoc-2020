def parse_rule(ipt):
    rule, letter, password = ipt.split(' ')
    low, high = rule.split('-')
    high = int(high)
    low = int(low)
    letter = letter[0]

    return low, high, letter, password


def part1(ipt):
    total = 0
    for l in ipt:
        low, high, letter, password = parse_rule(l)

        count = 0
        for char in password:
            if char == letter:
                count += 1
    
        if count >= low and count <= high:
            total += 1

    return total


def part2(ipt):
    total = 0
    for l in ipt:
        low, high, letter, password = parse_rule(l)

        if password[low - 1] == letter and password[high - 1] == letter:
            continue

        if password[low - 1] == letter or password[high - 1] == letter:
            total += 1

    return total


if __name__ == '__main__':
    with open('input.txt') as fp:
        ipt = [l for l in fp]
        print(part1(ipt))
        print(part2(ipt))