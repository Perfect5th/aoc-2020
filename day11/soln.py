def check_around(ipt, x, y):
    for x1 in range(x-1, x+2):
        if x1 < 0 or x1 >= len(ipt):
            continue

        for y1 in range(y-1, y+2):
            if y1 < 0 or y1 >= len(ipt[0]):
                continue

            if (x1, y1) == (x, y):
                continue

            if ipt[x1][y1] == '#':
                return False

    return True


def count_around(ipt, x, y):
    total = 0
    for x1 in range(x-1, x+2):
        if x1 < 0 or x1 >= len(ipt):
            continue

        for y1 in range(y-1, y+2):
            if y1 < 0 or y1 >= len(ipt[0]):
                continue

            if (x1, y1) == (x, y):
                continue

            if ipt[x1][y1] == '#':
               total += 1

    return total


def up(x, y):
    return x - 1, y

def right(x, y):
    return x, y + 1

def down(x, y):
    return x + 1, y

def left(x, y):
    return x, y - 1


directions = [
    up, right, down, left,
    lambda x, y: up(*right(x, y)), lambda x, y: up(*left(x, y)),
    lambda x, y: down(*right(x, y)),
    lambda x, y: down(*left(x, y)),
]

def move_dir(ipt, direction, x, y):
    while True:
        x, y = direction(x, y)
        
        if x < 0 or x >= len(ipt) or y < 0 or y >= len(ipt[0]):
            raise Exception("TOO FAR")

        yield x, y

def check_sight(ipt, x, y):
    for direction in directions:
        try:
            for x1, y1 in move_dir(ipt, direction, x, y):
                if ipt[x1][y1] == '#':
                    return False
                elif ipt[x1][y1] == 'L':
                    break
        except:
            pass
    
    return True


def count_sight(ipt, x, y):
    total = 0
    for direction in directions:
        try:
            for x1, y1 in move_dir(ipt, direction, x, y):
                if ipt[x1][y1] == '#':
                    total += 1
                    break
                elif ipt[x1][y1] == 'L':
                    break
        except:
            pass
    
    return total


def solve(ipt, should_fill, should_empty):
    while True:
        next_phase = [row[:] for row in ipt[:]]

        for x, row in enumerate(ipt):
            for y, seat in enumerate(row):
                if seat == 'L' and should_fill(ipt, x, y):
                    next_phase[x][y] = '#'
                elif seat == '#' and should_empty(ipt, x, y):
                    next_phase[x][y] = 'L'

        if all([row1 == next_phase[i] for i, row1 in enumerate(ipt)]):
            print(sum([1 for row in ipt for seat in row if seat == '#']))
            return
        
        ipt = next_phase


if __name__ == '__main__':
    for f, t in [('test_input.txt', True), ('input.txt', False)]:
        ipt = []
        
        with open(f) as fp:
            ipt = [list(l.rstrip('\n')) for l in fp]

        if t:
            print('TEST')
        else:
            print('RESULT')

        solve(ipt, check_around, lambda ipt, x, y: count_around(ipt, x, y) >= 4)
        solve(ipt, check_sight, lambda ipt, x, y: count_sight(ipt, x, y) >= 5)
        print('')