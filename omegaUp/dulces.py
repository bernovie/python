lim = int(raw_input())
nums = []
total = 0
for i in range(lim):
    nums.extend(map(int, raw_input().split()))
for i in range(0, len(nums)-1, +2):
    total += nums[i]*nums[i+1]
print total
