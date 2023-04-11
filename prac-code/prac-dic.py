def two_sum(nums, target):
    memo = {}
    for v in nums:
        memo[v] = True
    
