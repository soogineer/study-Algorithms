n = int(input())
x, y = 1, 1
directions = list(int.split())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0 ,0]
direct_types = ['L', 'R', 'U', 'D']

for direction in directions:
    for i in range(len(direct_types)):
      if directions == direct_types[i]:
        nx = x + dx[i]
        ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

n = 5
direct_types = ['R','R','R','U','D','D']
print(x, y)