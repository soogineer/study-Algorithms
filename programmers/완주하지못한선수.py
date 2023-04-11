#https://school.programmers.co.kr/learn/courses/30/lessons/42576

# dictionary 풀이

def solution(participant, completion):
    answer = ''
    part_dic = {}
    comp_dic = {}
    
     
    for v in participant:
        if v in part_dic:
            part_dic[v] += 1
        else:
            part_dic[v] = 1

    # 완주자 딕셔너리 
    for v in completion:
        if v in comp_dic:
            comp_dic[v] += 1
        else:
            comp_dic[v] = 1
            
    for v in participant:
        # 완주자 리스트에 참가자가 없을 경우
        if v not in comp_dic:
            answer = v
            
        # 참가자가 동명 이인일 경우
        if v in comp_dic:
            if part_dic[v] - comp_dic[v] == 1:
                answer = v

    return answer