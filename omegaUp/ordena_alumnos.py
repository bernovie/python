lim = int(raw_input())
cals = []
cals.extend(map(int, raw_input().split()))

for i in range(lim):
    for e in range(i, lim):
        if int(cals[i]) < int(cals[e]):
            temp = cals[i]
            cals[i] = cals[e]
            cals[e] = temp

for i in range(lim):
    print cals[i],
