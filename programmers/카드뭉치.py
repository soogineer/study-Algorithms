def solution(cards1, cards2, goal):
    answer = []
    n = len(cards1)
    m = len(cards2)
    
    i = j = 0
    for word in goal:
        if i < n and word == cards1[i]:
            answer.append(cards1[i])
            i += 1
            
        if j < m and word == cards2[j]:
            answer.append(cards2[j])
            j += 1
        
    return 'Yes' if answer == goal else 'No'
    

def solution(cards1, cards2, goal):
    answer = 'Yes'
    
    card1_idx, card2_idx = 0, 0
    
    for word in goal:
        if len(cards1) > card1_idx and word == cards1[card1_idx]:
            card1_idx += 1
        elif len(cards2) > card2_idx and word == cards2[card2_idx]:
            card2_idx += 1
        else:
            answer = "No"
            break
    
    return answer