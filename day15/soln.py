def solve(ipt, target):
    seen = {v: [i+1] for i, v in enumerate(ipt)}
    last = ipt[-1]

    for i in range(len(ipt) + 1, target + 1):
        if len(seen[last]) == 1:
            curr = 0
        else:
            curr = seen[last][-1] - seen[last][-2]

        if seen.get(curr):
            seen[curr].append(i)
        else:
            seen[curr] = [i]

        last = curr

    print(last)


def solve1(ipt, **kwargs):
    solve([int(i) for i in ipt[0].split(',')], 2020)


def solve2(ipt, **kwargs):
    solve([int(i) for i in ipt[0].split(',')], 30000000)