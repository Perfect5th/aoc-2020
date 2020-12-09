def solve(ipt, step):
    invalid = 0
    for i in range(step, len(ipt)):
        target = ipt[i]
        seen = set()
        valid = False

        for j in range(i-step, i):
            candidate = ipt[j]

            if target - candidate in seen and target != target - candidate:
                valid = True
            else:
                seen.add(candidate)

        if not valid:
            invalid = target
            print('part 1: %d' % target)
            break

    for i in range(len(ipt)):
        total = ipt[i]
        ran = [ipt[i]]
        for j in range(i+1, len(ipt)):
            ran.append(ipt[j])
            total += ipt[j]

            if total == invalid:
                print('part 2: %d' % (min(ran) + max(ran)))
            elif total > invalid:
                break


if __name__ == '__main__':
    for f, s, t in [('test_input.txt', 5, True), ('input.txt', 25, False)]:
        ipt = []
        
        with open(f) as fp:
            ipt = [int(l.rstrip('\n')) for l in fp]

        if t:
            print('TEST')
        else:
            print('RESULT')

        solve(ipt, s)
        print('')