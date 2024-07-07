import sys
sys.setrecursionlimit(10000)

n = int(input())

grid = [
    list(map(int,input().split()))
    for _ in range(n)
]

visited=[
    [False for _ in range(n)] for _ in range(n)
]

def in_range(i,j):
    return 0 <= i < n and 0 <= j < n
def can_go(i,j):
    if in_range(i,j) == False: return False
    if visited[i][j]: return False
    return True

def dfs(i,j,num):
    global area
    dxs,dys= [0,0,1,-1],[1,-1,0,0]
    for dx,dy in zip(dxs,dys):
        nx, ny = dx+i, dy+j
        if can_go(nx,ny) and grid[nx][ny] == num:
            visited[i][j] = True
            area+=1
            dfs(nx,ny,num)

cnt = 0
max_area = 1
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            num = grid[i][j]
            area = 1
            dfs(i,j,num)
            if 4 <= area: cnt+=1
            if max_area < area : max_area = area

print(cnt, max_area)