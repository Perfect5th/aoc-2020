def solve(ipt):
    next_phase = ipt[:]
    for i, row in enumerate(ipt):
        for j, seat in enumerate(row):
            up = ipt[i-1][j] if i > 0 else None
            lup = ipt[i-1][j-1] if i > 0 and j > 0 else None
            rup = ipt[i-1][j+1] if i > 0 and j < len(row) - 1 else None
            right = ipt[i][j+1] if j < len(row) - 1 else None
            down = ipt[i+1][j] if i < len(ipt) - 1 else None
            ldown = ipt[i+1][j-1] if i < len(ipt) - 1 and j > 0 else None
            rdown = ipt[i+1][j+1] if i < len(ipt) - 1 and j < len(row) - 1 else None
            left = ipt[i][j-1] if j > 0 else None

            if seat == 'L' and all([x is None or x == '.' or x == 'L' for x in [up, right, down, left, ldown, lup, rdown, rup]]):
                next_phase[i] = next_phase[i][:j] + '#' + (next_phase[i][j+1:] if j < len(row) - 1 else '')
            elif seat == '#' and sum([1 for x in [up, right, down, left, ldown, lup, rdown, rup] if x == '#']) >= 4:
                next_phase[i] = next_phase[i][:j] + 'L' + (next_phase[i][j+1:] if j < len(row) - 1 else '')

    if ipt == next_phase:
        total = 0
        for row in ipt:
            for seat in row:
                if seat == '#':
                    total += 1

        print(total)
        return
    
    solve(next_phase)


def see_none(ipt, i, j):
    i1 = i + 1
    while i1 < len(ipt):
        if ipt[i1][j] == '#':
            return False
        elif ipt[i1][j] == 'L':
            break
        i1 += 1

    i1 = i - 1
    while i1 >= 0:
        if ipt[i1][j] == '#':
            return False
        elif ipt[i1][j] == 'L':
            break
        i1 -= 1

    j1 = j - 1
    while j1 >= 0:
        if ipt[i][j1] == '#':
            return False
        elif ipt[i][j1] == 'L':
            break
        j1 -= 1

    j1 = j + 1
    while j1 < len(ipt[0]):
        if ipt[i][j1] == '#':
            return False
        elif ipt[i][j1] == 'L':
            break
        j1 += 1

    i1 = i + 1
    j1 = j + 1
    while i1 < len(ipt) and j1 < len(ipt[0]):
        if ipt[i1][j1] == '#':
            return False
        elif ipt[i1][j1] == 'L':
            break
        i1 += 1
        j1 += 1

    i1 = i - 1
    j1 = j - 1
    while i1 >= 0 and j1 >= 0:
        if ipt[i1][j1] == '#':
            return False
        elif ipt[i1][j1] == 'L':
            break
        i1 -= 1
        j1 -= 1

    i1 = i - 1
    j1 = j + 1
    while i1 >= 0 and j1 < len(ipt[0]):
        if ipt[i1][j1] == '#':
            return False
        elif ipt[i1][j1] == 'L':
            break
        i1 -= 1
        j1 += 1
    
    i1 = i + 1
    j1 = j - 1
    while i1 < len(ipt) and j1 >= 0:
        if ipt[i1][j1] == '#':
            return False
        elif ipt[i1][j1] == 'L':
            break
        i1 += 1
        j1 -= 1

    return True


def see_some(ipt, i, j):
    total = 0

    i1 = i + 1
    while i1 < len(ipt):
        if ipt[i1][j] == '#':
            total += 1
            break
        elif ipt[i1][j] == 'L':
            break
        i1 += 1

    i1 = i - 1
    while i1 >= 0:
        if ipt[i1][j] == '#':
            total += 1
            break
        elif ipt[i1][j] == 'L':
            break
        i1 -= 1

    j1 = j - 1
    while j1 >= 0:
        if ipt[i][j1] == '#':
            total += 1
            break
        elif ipt[i][j1] == 'L':
            break
        j1 -= 1

    j1 = j + 1
    while j1 < len(ipt[0]):
        if ipt[i][j1] == '#':
            total += 1
            break
        elif ipt[i][j1] == 'L':
            break
        j1 += 1

    i1 = i + 1
    j1 = j + 1
    while i1 < len(ipt) and j1 < len(ipt[0]):
        if ipt[i1][j1] == '#':
            total += 1
            break
        elif ipt[i1][j1] == 'L':
            break
        i1 += 1
        j1 += 1

    i1 = i - 1
    j1 = j - 1
    while i1 >= 0 and j1 >= 0:
        if ipt[i1][j1] == '#':
            total += 1
            break
        elif ipt[i1][j1] == 'L':
            break
        i1 -= 1
        j1 -= 1

    i1 = i - 1
    j1 = j + 1
    while i1 >= 0 and j1 < len(ipt[0]):
        if ipt[i1][j1] == '#':
            total += 1
            break
        elif ipt[i1][j1] == 'L':
            break
        i1 -= 1
        j1 += 1
    
    i1 = i + 1
    j1 = j - 1
    while i1 < len(ipt) and j1 >= 0:
        if ipt[i1][j1] == '#':
            total += 1
            break
        elif ipt[i1][j1] == 'L':
            break
        i1 += 1
        j1 -= 1

    return total


def solve2(ipt):
    while True:
        next_phase = ipt[:]
        for i, row in enumerate(ipt):
            for j, seat in enumerate(row):
                if seat == 'L' and see_none(ipt, i, j):
                    next_phase[i] = next_phase[i][:j] + '#' + (next_phase[i][j+1:] if j < len(row) - 1 else '')
                elif seat == '#' and see_some(ipt, i, j) >= 5:
                    next_phase[i] = next_phase[i][:j] + 'L' + (next_phase[i][j+1:] if j < len(row) - 1 else '')

        if ipt == next_phase:
            total = 0
            for row in ipt:
                for seat in row:
                    if seat == '#':
                        total += 1

            print(total)
            return
        
        ipt = next_phase
    


if __name__ == '__main__':
    for f, t in [('test_input.txt', True), ('input.txt', False)]:
        ipt = []
        
        with open(f) as fp:
            ipt = [l.rstrip('\n') for l in fp]

        if t:
            print('TEST')
        else:
            print('RESULT')

        solve(ipt)
        solve2(ipt)
        print('')