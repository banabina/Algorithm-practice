import sys

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
check = [False for _ in range(n + 1)]

for _ in range(m):
    v1, v2 = map(int, sys.stdin.readline().strip().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

def dfs(x):
    check[x] = True
    for next in graph[x]:
        if not check[next]:
            dfs(next)

dfs(1)
cnt = 0
for i in range(2, n + 1):
    if check[i]:
        cnt += 1
print(cnt)