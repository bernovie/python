max = int(raw_input())
sum = []
for i in range(max):
    a, b = map(int, raw_input().split())
    sum.append(a + b)

for i in range(max):
    print sum[i]
