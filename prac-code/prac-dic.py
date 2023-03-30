def two_sum(nums, target):
    memo = {}
    for v in nums:
        memo[v] = True
    for v in nums:
      needed_number = target - v
      if needed_number in memo:
        return True
    return False
