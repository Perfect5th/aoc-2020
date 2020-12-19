def solve1(ipt, target=2020, print_result=True):
    ipt = map(lambda i: int(i), ipt)
    seen = set()

    for x in ipt:
        if target - x in seen:
            result = x * (target - x)

            if print_result:
                print(result)

            return result

        seen.add(x)

    raise Exception("Couldn't find a match")


def solve2(ipt):
    ipt = [int(i) for i in ipt]
    target = 2020

    for x in ipt:
        try:
            print(solve1(ipt, target - x, False) * x)
            return
        except:
            continue

    raise Exception("Couldn't find a match")