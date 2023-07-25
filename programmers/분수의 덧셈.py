# https://school.programmers.co.kr/learn/courses/30/lessons/120808

def solution(denum1, num1, denum2, num2):
    answer = []
    num = denum1*num2 + denum2*num1 # 분자
    deno = num2*num1                # 분모

    gcd = 0
    # num과 deno의 최대공약수 구하기
    for j in range(min(num,deno), 0, -1):
        if num % j == 0 and deno % j ==0:
            gcd = j
            break
    
    answer = [num//gcd, deno//gcd]
    return answer

#2
def solution(answers):
    counts = [0,0,0]
    winner = []
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5,]
    
    for i in range(len(answers)):
        if answers[i] == s1[(i%5)]:
            counts[0] += 1
        if answers[i] == s2[(i%8)]:
            counts[1] += 1
        if answers[i] == s3[(i%10)]:
            counts[2] += 1
            
    for i in range(3):
        if counts[i] == max(counts):
            winner.append(i+1)

    return winner