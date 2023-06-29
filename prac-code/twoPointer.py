def twoSum(nums, target):
    nums.sort() # nums 정렬
    l, r = 0, len(nums)-1

    while l < r:
          if target < nums[l] + nums[r]:
            r -= 1
          elif target > nums[l] + nums[r]:
            l += 1
          elif target == nums[l] + nums[r]:
              return True
    return False