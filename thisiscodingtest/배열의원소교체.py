n, k = map(int, input().split())
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

def solution(n, k, arr_a, arr_b):
    answer = 0
    arr_a.sort()
    arr_b.sort(reverse=True)

    for i in range(k):
        if arr_a[i] < arr_b[i]:
          arr_a[i], arr_b[i] = arr_b[i], arr_a[i]
        else:
          break
    answer = sum(arr_a)
    return answer


print(solution(n=5, k=3, arr_a=[1, 2, 5, 4, 3], arr_b=[5, 5, 6, 6, 5]))