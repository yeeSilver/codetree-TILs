import sys
sys.setrecursionlimit(10000)
n, m = tuple(map(int, input().split()))
grid =[]
for _ in range(n):
    grid.append(list(map(int,input().split())))
visited=[
    [False for _ in range(m)]
    for _ in range(n)
]

def dfs(i,j):
    dxs,dys = [0,1], [1,0]
    for x,y in zip (dxs,dys):
        nx,ny = x+i, y+j
        if 0 <= nx <n and 0<= ny < m:
            if grid[nx][ny] == 1 and visited[nx][ny] ==False:
                visited[nx][ny]=True
                
                if nx==n-1 and ny ==m-1: return 1
                if dfs(nx,ny)==1: return 1

if dfs(0,0) ==1 : print(1)
else: print(0)