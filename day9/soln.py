def solve1(ipt, print_result=True, **kwargs):
    ipt = [int(i) for i in ipt]
    step = 5 if kwargs.get('is_test') else 25

    invalid = 0
    for i in range(step, len(ipt)):
        target = ipt[i]
        seen = set()
        valid = False

        for j in range(i-step, i):
            candidate = ipt[j]

            if target - candidate in seen and target != target - candidate:
                valid = True
                break
            else:
                seen.add(candidate)

        if not valid:
            invalid = target

            if print_result:
                print(target)

            return invalid

def solve2(ipt, **kwargs):
    invalid = solve1(ipt, False, **kwargs)
    ipt = [int(i) for i in ipt]

    for i in range(len(ipt)):
        total = ipt[i]
        ran = [ipt[i]]
        for j in range(i+1, len(ipt)):
            ran.append(ipt[j])
            total += ipt[j]

            if total == invalid:
                print((min(ran) + max(ran)))
                return
            elif total > invalid:
                break