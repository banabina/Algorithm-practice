from collections import deque
import sys

n, m, start = map(int, sys.stdin.readline().strip().split())

edge = [[] for _ in range(n + 1)]

for _ in range(m):
    v1, v2 = map(int, sys.stdin.readline().strip().split())
    edge[v1].append(v2)
    edge[v2].append(v1)

for e in edge:
    e.sort(reverse=True)

def dfs():
    d_visit = []
    d_check = [0 for _ in range(n + 1)]
    stack = [start]
    while stack:
        v = stack.pop()
        if not d_check[v]:
            d_check[v] = 1
            d_visit.append(v)
            stack += edge[v]
    return d_visit

def bfs():
    b_visit = []
    queue = deque([start])
    b_check = [0 for _ in range(n + 1)]
    b_check[start] = 1
    while queue:
        v = queue.popleft()
        b_visit.append(v)
        for i in reversed(edge[v]):
            if not b_check[i]:
                b_check[i] = 1
                queue.append(i)
    return b_visit

print(' '.join(map(str,dfs())))
print(' '.join(map(str,bfs())))
