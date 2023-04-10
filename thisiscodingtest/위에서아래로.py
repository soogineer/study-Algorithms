n = int(input())

arr =[]
for i in range(n):
    arr.append(int(input()))

def solution(n, arr):
    arr.sort(reverse=True)
    return arr

print(solution(n, arr))
