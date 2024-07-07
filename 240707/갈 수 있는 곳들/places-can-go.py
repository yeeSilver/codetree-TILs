from collections import deque
q = deque()

n,k = map(int,input().split())
grid=[
    list(map(int,input().split()))
    for _ in range(n)
]
visited=[
    [False for _ in range(n)] for _ in range(n)
]

def in_range(r,c):
    return 0<=r<n and 0<=c<n
def can_go(r,c):
    if not in_range(r,c): return False
    if visited[r][c]: return False
    if grid[r][c] == 1: return False
    return True

def bfs(x,y):
    global area

    dxs,dys= [0,0,-1,1],[1,-1,0,0]
    for i in range(4):
        nx = x+dxs[i]
        ny = y+dys[i]
        if can_go(nx,ny):
            visited[nx][ny]=True
            area+=1

def initalized():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

area = 0
for _ in range(k):
    r,c = map(int,input().split())
    r-=1
    c-=1

    initalized()

    if can_go(r,c):
        visited[r][c]=True
        area+=1
        bfs(r,c)
print(area)