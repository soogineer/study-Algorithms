n, m = map(int, input().split())
h = list(map(int, input().split()))

start = 0
end = max(h)

while True:
    if start > end:
        break

    median = (start + end) // 2
    target = sum([i - median if (i-median) > 0 else 0 for i in h])

    if m == target:
        print(median)
        break
        
    if m < target:
        start = median + 1
    else:
        end = median - 1