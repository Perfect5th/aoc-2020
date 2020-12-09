ipt = []
with open('input.txt') as fp:
    ipt = [int(l) for l in fp]

step = 25
invalid = 0
for i in range(step, len(ipt)):
    prev = ipt[i-step:i]

    valid = False
    for j in prev:
        for k in prev:
            if j == k:
                continue
        
            if j+k == ipt[i]:
                valid = True

    if not valid:
        invalid = ipt[i]
        print(ipt[i])
        break

for i in range(len(ipt)):
    total = ipt[i]
    ran = [ipt[i]]
    for j in range(i+1, len(ipt)):
        ran.append(ipt[j])
        total += ipt[j]

        if total == invalid:
            print(min(ran) + max(ran))
        elif total > invalid:
            break
