lim = int(raw_input())
nums = []
nums = map(int, raw_input().split())
max = nums[0]
for i in range(lim):
    if nums[i] > max:
        max = nums[i]
print max
