def solve1(ipt):
    ipt = sorted(ipt)
    
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


def solve2(ipt):
    memo = [0 for _ in ipt]
    for i, v in enumerate(ipt[:3]):
        if v <= 3:
            memo[i] += 1

    for i, v in enumerate(ipt[:-1]):
        for j, w in enumerate(ipt[i+1:i+4]):
            if w <= v + 3:
                memo[j+i+1] += memo[i]

    print(memo[-1])


if __name__ == '__main__':
    for f, t in [('test_input.txt', True), ('input.txt', False)]:
        ipt = []
        
        with open(f) as fp:
            ipt = [int(l.rstrip('\n')) for l in fp]

        if t:
            print('TEST')
        else:
            print('RESULT')

        solve1(ipt)
        solve2(sorted(ipt))
        print('')