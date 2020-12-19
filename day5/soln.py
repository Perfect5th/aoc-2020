def to_binary(ticket):
    ticket = ticket.replace('F', '0')
    ticket = ticket.replace('B', '1')
    ticket = ticket.replace('L', '0')
    ticket = ticket.replace('R', '1')

    return int(ticket, 2)


def part1(ipt):
    return max([to_binary(ticket) for ticket in ipt])


def part2(ipt):
    ipt = [to_binary(t) for t in ipt]

    for i in range(1, len(ipt) - 1):
        if ipt[i-1] != ipt[i] - 1 and ipt[i+1] != ipt[i] + 1:
            return ipt[i]

    return 0


if __name__ == '__main__':
    with open('input.txt') as fp:
        print(part1(fp))
        fp.seek(0)
        print(part2(fp))
