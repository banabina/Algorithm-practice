import sys
from collections import deque

# 입력
n, m = map(int, input().split())

miro = []
dist = [[-1] * m for _ in range(n)] 
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n):
    miro.append(list(map(int, sys.stdin.readline().strip())))

# bfs
queue = deque()
queue.append((0, 0))
dist[0][0] = 1
while queue:
    cur = queue.popleft()
    x = cur[0]
    y = cur[1]
    for i in range(4):
        nx = cur[0] + dx[i]
        ny = cur[1] + dy[i]
        if nx >= 0 and ny >=0 and nx < n and ny < m:
            if dist[nx][ny] == -1 and miro[nx][ny] == 1:
                queue.append((nx, ny))
                dist[nx][ny] = dist[x][y] + 1

print(dist[n-1][m-1])