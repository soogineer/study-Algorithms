# https://school.programmers.co.kr/learn/courses/30/lessons/136798

def solution(number, limit, power):
    answer = 0
    weapon_weights = [0] * (number + 1)  # 각 기사의 약수 개수에 해당하는 무기의 무게를 저장할 리스트

    # 약수 개수 계산
    for i in range(1, number + 1):
        for j in range(i, number + 1, i):
            weapon_weights[j] += 1

    # 무기점에서 무기를 구매하여 필요한 철의 무게 계산
    for i in range(1, number + 1):
        if weapon_weights[i] > limit:
            answer += power
        else:
            answer += weapon_weights[i]

    return answer
