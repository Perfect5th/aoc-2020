def to_binary(ticket):
    ticket = ticket.replace('F', '0')
    ticket = ticket.replace('B', '1')
    ticket = ticket.replace('L', '0')
    ticket = ticket.replace('R', '1')

    return ticket


def part1(ipt):
    maximum = 0
    
    for t in ipt:
        as_binary = to_binary(t)

        seatid = int(as_binary, 2) 

        if seatid > maximum:
            maximum = seatid

    return maximum


def part2(ipt):
    all_seats = range(0, 0b10000000000)

    for t in ipt:
        as_binary = int(to_binary(t), 2)

        all_seats = [x for x in all_seats if x != as_binary]

    for i, s in enumerate(all_seats):
        if i == 0 or i == len(all_seats) - 1:
            continue

        if s != all_seats[i+1] - 1 and s != all_seats[i-1] + 1:
            return s

    return list(all_seats)


if __name__ == '__main__':
    with open('input.txt') as fp:
        print(part1(fp))
        fp.seek(0)
        print(part2(fp))
