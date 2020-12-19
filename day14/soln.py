def solve1(ipt, **kwargs):
    mem = {}
    mask = ipt[0][7:]

    for l in ipt[1:]:
        if 'mask' in l:
            mask = l[7:]
            continue

        loc, val = l.split('=')
        loc = loc.rstrip(' ')
        loc = int(loc.split('[')[1].split(']')[0])
        val = val.lstrip(' ')
        val = int(val)

        valbin = str(bin(val))[2:]
        valrev = list(reversed(valbin))
        maskrev = list(reversed(mask))

        masked = []
        for i, v in enumerate(maskrev):
            if v == 'X':
                try:
                    masked.append(valrev[i])
                except Exception:
                    masked.append('0')
            else:
                masked.append(v)

        mem[loc] = int(''.join(reversed(masked)), 2)

    print(sum([v for k, v in mem.items()]))


def solve2(ipt, **kwargs):
    mem = {}
    mask = ipt[0][7:]

    for l in ipt[1:]:
        if 'mask' in l:
            mask = l[7:]
            continue

        loc, val = l.split('=')
        loc = loc.rstrip(' ')
        loc = int(loc.split('[')[1].split(']')[0])
        val = val.lstrip(' ')
        val = int(val)

        locbin = str(bin(loc))[2:]
        locrev = list(reversed(locbin))
        maskrev = list(reversed(mask))

        masked = []
        for i, v in enumerate(maskrev):
            if maskrev[i] == '0':
                try:
                    masked.append(locrev[i])
                except Exception:
                    masked.append('0')
            else:
                masked.append(maskrev[i])

        locs = [['0']]
        for a in reversed(masked):
            if a == 'X':
                for l in range(len(locs)):
                    locs.append(locs[l][:])

                for l in range(len(locs)//2):
                    locs[l].append('0')
                for l in range(len(locs)//2, len(locs)):
                    locs[l].append('1')
            else:
                for l in range(len(locs)):
                    locs[l].append(a)

        for l in locs:
            mem[int(''.join(l), 2)] = val

    print(sum([v for k, v in mem.items()]))