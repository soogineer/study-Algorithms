def dailiyTemperatures(temperatures):
    ans = [0] * len(temperatures) # 배열을 0으로 설정
    stack = [] #stack 선언
    for cur_day, cur_temp in enumerate(temperatures):
        while stack and stack[-1][1] < cur_temp:
            prev_day, _ = stack.pop() # _는 prev_temp 값 반환 안 시키게 함
            ans[prev_day] = cur_day - prev_day
        stack.append((cur_day, cur_temp))
    return ans

dailyTemperatures = ([73,74,75,71,69,72,76,73])