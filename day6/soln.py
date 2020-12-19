from utils import input_groups


qs = [chr(ord('a')+i) for i in range(26)]


def read_card(ipt):
    card = ''
    for l in ipt:
        if l == '\n':
            yield card
            card = ''
        
        card += l


def solve1(ipt):
    total = 0

    for card in input_groups(ipt):
        answered = 0

        for q in qs:
            if any(map(lambda p: q in p, card)):
                answered += 1

        total += answered

    print(total)


def solve2(ipt):
    total = 0

    for card in input_groups(ipt):
        answered = 0
        counts = {i: 0 for i in qs}

        for r in card:
            for q in r:
                counts[q] += 1

        for _, v in counts.items():
            if v == len(card):
                answered += 1

        total += answered

    print(total)