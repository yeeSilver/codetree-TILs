import sys
sys.setrecursionlimit(10000)
n ,m = tuple(map(int, input().split()))

graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]



for _ in range(m):
    s,e = tuple(map(int,input().split()))
    graph[s].append(e)
    graph[e].append(s)

cnt = 0
def dfs(root):
    global cnt
    for vertex in graph[root]:
        if visited[vertex] == 0:
            visited[vertex] =1
            cnt +=1
            dfs(vertex)
dfs(1)
print(cnt - 1)