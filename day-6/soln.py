qs = [chr(ord('a')+i) for i in range(26)]

def read_card(ipt):
    card = ''
    for l in ipt:
        if l == '\n':
            yield card
            card = ''
        
        card += l


def part1(ipt):
    total = 0

    for card in read_card(ipt):
        answered = 0

        for q in qs:
            if q in card:
                answered += 1

        total += answered

    return total


def part2(ipt):
    total = 0

    for card in read_card(ipt):
        answered = 0
        counts = {i: 0 for i in qs}

        res = card.split('\n')

        for r in res:
            for q in r:
                counts[q] += 1

        for k, v in counts.items():
            if v == len(res) - 2:
                answered += 1

        total += answered

    return total


if __name__ == '__main__':
    with open('input.txt') as fp:
        print(part1(fp))
        fp.seek(0)
        print(part2(fp))
