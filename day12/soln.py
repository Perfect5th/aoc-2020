import math

def solve(ipt):
    parsed = [(i[0], int(i[1:])) for i in ipt]
    position = [0, 0, 90]

    for d, v in parsed:
        if d == 'N':
            position[0] += v
        elif d == 'E':
            position[1] += v
        elif d == 'S':
            position[0] -= v
        elif d == 'W':
            position[1] -= v
        elif d == 'L':
            position[2] -= v
        elif d == 'R':
            position[2] += v
        elif d == 'F':
            rads = position[2] * math.pi / 180
            x = math.cos(rads) * v
            y = math.sin(rads) * v
            position[0] += x
            position[1] += y

    print(round(abs(position[0]) + abs(position[1])))

def solve2(ipt):
    parsed = [(i[0], int(i[1:])) for i in ipt]
    position = [1, 10]
    ship = [0, 0]

    for d, v in parsed:
        if d == 'N':
            position[0] += v
        elif d == 'E':
            position[1] += v
        elif d == 'S':
            position[0] -= v
        elif d == 'W':
            position[1] -= v
        elif d == 'L':
            quarters = v // 90
            for i in range(quarters):
                n = position[0]
                position[0] = position[1]
                position[1] = -1 * n
        elif d == 'R':
            quarters = v // 90
            for i in range(quarters):
                n = position[0]
                position[0] = -1 * position[1]
                position[1] = n
        elif d == 'F':
            ship[0] += position[0] * v
            ship[1] += position[1] * v

    print(round(abs(ship[0]) + abs(ship[1])))


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