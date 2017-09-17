lim = int(raw_input())
nums = map(int, raw_input().split())

for i in range(len(nums)):
    for e in range(i+1, len(nums)):
        if nums[i] > nums[e]:
            print "NO"
            exit()

print "SI"
