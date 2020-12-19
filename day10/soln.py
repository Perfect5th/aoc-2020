def solve1(ipt, **kwargs):
    ipt = sorted([int(i) for i in ipt])
    
    curr = 0
    ones = 0
    threes = 0
    for i in ipt:
        diff = i - curr

        if diff == 3:
            threes += 1
        elif diff == 1:
            ones += 1
        
        curr = i

    threes += 1
    print(threes * ones)


def solve2(ipt, **kwargs):
    memo = [0 for _ in ipt]
    ipt = sorted([int(i) for i in ipt])

    for i, v in enumerate(ipt[:3]):
        if v <= 3:
            memo[i] += 1

    for i, v in enumerate(ipt[:-1]):
        for j, w in enumerate(ipt[i+1:i+4]):
            if w <= v + 3:
                memo[j+i+1] += memo[i]

    print(memo[-1])