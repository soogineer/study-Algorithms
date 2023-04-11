# https://leetcode.com/problems/longest-consecutive-sequence/


def longestConsecutive(nums):
    longest = 0
    num_dic = {} # 딕셔너리 적용
    for num in nums:
        num_dic[num] = True # num 값 입력해줌
    for num in num_dic:
        if num -1 not in num_dic: # 만약 num 전의 값이 딕셔너리에 존재하지 않는다면,
            count = 1
            target = num + 1
        while target in num_dic: # 딕셔너리에 target이 있는지 훑어줌
            count += 1
            target += 1 
        longest = max(longest, count)
    return longest
            

longestConsecutive([6, 7, 100, 5, 4, 4]) 