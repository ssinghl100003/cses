n = int(input())
nums = list(map(int, input().split()))
moves = 0
i = 1
while i < n:
    diff = nums[i-1] - nums[i]
    if diff > 0:
        nums[i] += diff
        moves += diff
    i += 1
print(moves)