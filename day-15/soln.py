def solve(ipt, target):
    ipt = [int(i) for i in ipt[0].split(',')]

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


if __name__ == '__main__':
    with open('test_input.txt') as test1:
        print('TEST1')
        solve([l.rstrip('\n') for l in test1], 10)
        print('')

    with open('input.txt') as ipt:
        print('RESULT')
        solve([l.rstrip('\n') for l in ipt], 2020)
        solve([l.rstrip('\n') for l in ipt], 30000000)
        print('')
