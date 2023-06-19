# https://school.programmers.co.kr/learn/courses/30/lessons/135808

def solution(k, m, score):
    answer = 0
    score.sort(reverse = True)
    
    for i in range(0, len(score), m):
        tmp = score[i:i+m]
        
        if len(tmp) == m:
            answer += min(tmp) * m
        
        
    return answer