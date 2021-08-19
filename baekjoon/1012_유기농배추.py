import sys
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def valid(row, col):
    return (row >= 0 and col >= 0 and row < n and col < m)

def dfs(row, col):
    check[row][col] = True
    for k in range(4):
        nx = row + dx[k]
        ny = col + dy[k]
        if valid(nx, ny) and not check[nx][ny] and graph[nx][ny] == 1:
            dfs(nx, ny)

T = int(input())
for __ in range(T):
    m, n, k = map(int, sys.stdin.readline().strip().split())
    graph = [[0] * m for _ in range(n)]
    check = [[False] * m for _ in range(n)]
    for i in range(k):
        v1, v2 = map(int, sys.stdin.readline().strip().split())
        graph[v2][v1] = 1
    ans = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0 or check[i][j]:
                continue
            ans += 1
            dfs(i, j)
    print(ans)
