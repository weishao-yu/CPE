def function(nums):
    n = nums.pop(0)
    s = set()
    for i in range(n - 1):
        x = abs(nums[i] - nums[i + 1])
        s.add(x)
    for i in range(1, n):
        if i not in s:
            return False
    return True
while True:
    try:
        nums = list(map(int, input().split()))
        if function(nums):
            print("Jolly")
        else:
            print("Not jolly")
    except EOFError:
        break 