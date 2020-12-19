def solve(ipt):
    earliest = int(ipt[0])
    buses = [int(i) for i in ipt[1].split(',') if i != 'x']
    count = 0
    times = {}

    while True:
        for bus in buses:
            if earliest % bus == 0:
                times[earliest] = bus
                count += 1
            
        earliest += 1
        if count >= len(buses):
            break

    print((min(times.keys()) - int(ipt[0])) * times[min(times.keys())])
    buses = ipt[1].split(',')

    start = int(buses[0])
    increment = int(buses[0])
    i = 1
    while True:
        if i >= len(buses):
            break

        b = buses[i]

        if b == 'x':
            i += 1
            continue

        b = int(b)

        if (start + i) % b == 0:
            increment *= b
            i += 1
            continue

        start += increment

    print(start)


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
        print('')