from collections import deque

def bfs(root):
  visited = []
  if root is None:
    return 0;
  q = deque()
  q.append(root)
  while q:
    cur_node = q.popleft()
    visited.append(cur_node.value)
