def get_neighbours(point):
    x, y, z = point[:3]
    w = None
    if len(point) == 4:
        w = point[3]

    for x1 in range(x-1, x+2):
        for y1 in range(y-1, y+2):
            for z1 in range(z-1, z+2):
                if len(point) == 4:
                    for w1 in range(w-1, w+2):
                        if (x1, y1, z1, w1) == (x, y, z, w):
                            continue

                        yield (x1, y1, z1, w1)
                else:
                    if (x1, y1, z1) == (x, y, z):
                        continue

                    yield (x1, y1, z1)


def solve(ipt, dimensions=3):
    points = {}

    for x in range(len(ipt)):
        for y in range(len(ipt[x])):
            key = (x, y, 0) if dimensions == 3 else (x, y, 0, 0)
            points[key] = ipt[x][y]

    for _ in range(6):
        phase_points = {}
        for k, v in points.items():
            phase_points[k] = v
            for n in get_neighbours(k):
                if n in phase_points:
                    continue

                phase_points[n] = '.'

        next_phase = {k: v for k, v in phase_points.items()}

        for point, val in phase_points.items():
            neighbor_count = sum([1 for n in get_neighbours(point) if phase_points.get(n, '.') == '#'])

            if val == '#' and not neighbor_count in range(2, 4):
                next_phase[point] = '.'
            elif val == '.' and neighbor_count == 3:
                next_phase[point] = '#'

        points = {k: v for k, v in next_phase.items()}

    print(sum([1 for v in points.values() if v == '#']))



if __name__ == '__main__':
    with open('test_input.txt') as test1:
        print('TEST1')
        i = [list(l.rstrip('\n')) for l in test1]
        solve(i)
        solve(i, 4)
        print('')

    with open('input.txt') as ipt:
        print('RESULT')
        i = [list(l.rstrip('\n')) for l in ipt]
        solve(i)
        solve(i, dimensions=4)
        print('')
