def solution(n, quests):
    graph = [[] for _ in range(n+1)] # 퀘스트 간의 선행관계를 표현하기 위한 그래프
    in_degree = [0] * (n+1) # 각 퀘스트의 진입차수를 저장하는 배열
    
    # 그래프와 진입차수 구성
    for quest in quests:
        a, b = quest
        graph[a].append(b)
        in_degree[b] += 1
    
    answer = [] # 퀘스트 클리어 순서 리스트로 저장
    queue = []
    
    # 진입차수가 0인 퀘스트들을 큐에 삽입
    for i in range(1, n+1):
        if in_degree[i] == 0:
            queue.append(i)
    
    # 위상 정렬 수행
    while queue:
        node = queue.pop(0)
        answer.append(node)
        
        for next_node in graph[node]:
            in_degree[next_node] -= 1
            if in_degree[next_node] == 0:
                queue.append(next_node)
    
    return answer
