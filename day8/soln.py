def run_prgm(ipt):
    run = [False for i in ipt]
    pc = 0
    acc = 0

    while not run[pc] and pc < len(ipt) - 1:
        curr = ipt[pc]
        inst, val = curr.split(' ')
        val = int(val)
        run[pc] = True

        if inst == 'acc':
            acc += val
            pc += 1
        elif inst == 'jmp':
            pc += val
        else:
            pc += 1

    if pc >= len(ipt) - 1:
        return 'terminated', acc

    return 'looped', acc


def part1(ipt):
    return run_prgm(ipt)[1]


def part2(ipt):
    for i in range(len(ipt)):
        inst, val = ipt[i].split(' ')
        new_ipt = ipt[:]

        if inst == 'jmp':
            new_ipt[i] = 'nop ' + val
        elif inst == 'nop':
            new_ipt[i] = 'jmp ' + val 

        result, acc = run_prgm(new_ipt)

        if result == 'terminated':
            return acc


if __name__ == '__main__':
    with open('input.txt') as fp:
        ipt = [l for l in fp]
        print(part1(ipt))
        print(part2(ipt))
