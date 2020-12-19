def to_binary(ticket):
    ticket = ticket.replace('F', '0')
    ticket = ticket.replace('B', '1')
    ticket = ticket.replace('L', '0')
    ticket = ticket.replace('R', '1')

    return int(ticket, 2)


def solve1(ipt):
    print(max([to_binary(ticket) for ticket in ipt]))


def solve2(ipt):
    ipt = sorted([to_binary(t) for t in ipt])

    for i in range(1, len(ipt) - 1):
        if ipt[i-1] != ipt[i] - 1 or ipt[i+1] != ipt[i] + 1:
            if ipt[i-1] != ipt[i] - 1:
                print(ipt[i]-1)
            else:
                print(ipt[i]+1)
            return

    raise Exception("Couldn't find the answer.")