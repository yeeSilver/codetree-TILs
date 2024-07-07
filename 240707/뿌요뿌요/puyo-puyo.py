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
        if can_go(nx, ny) and grid[nx][ny] == num:
            visited[nx][ny] = True
            area+=1
            dfs(nx,ny,num)

bomb_cnt = 0
max_area = -sys.maxsize

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            visited[i][j]=True
            num = grid[i][j]
            area = 1
            dfs(i,j,num)
            if 4 <= area:
                bomb_cnt+=1
            max_area = max(area,max_area)
            # print(max_area)


print(bomb_cnt, max_area)