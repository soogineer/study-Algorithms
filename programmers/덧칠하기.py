def solution(n, m, section):
    painted = [0]*(n+1)

    for sec in section:
        painted[sec] = 1
    count = 0
    
    for i in range(1, n + 1):
        if painted[i] == 1:
            count += 1
        else:
            if painted[i - 1] == 1:
                count += 1
        
    return count