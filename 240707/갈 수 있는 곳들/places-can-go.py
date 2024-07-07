from collections import deque
q = deque()

n,k = map(int,input().split())
grid=[
    list(map(int,input().split()))
    for _ in range(n)
]
visited=[
    [0 for _ in range(n)] for _ in range(n)
]

def in_range(r,c):
    return 0<=r<n and 0<=c<n
def can_go(r,c,k):
    if not in_range(r,c): return False
    # print(r,c, visited[r][c])
    if visited[r][c] == k: return False
    if grid[r][c] == 1: return False
    return True

def bfs(k):
    while q:
        x,y = q.popleft()
        dxs,dys= [0,0,-1,1],[1,-1,0,0]
        for dx,dy in zip(dxs,dys):
            nx = x+dx
            ny = y+dy
            if can_go(nx,ny,k):
                visited[nx][ny]=k
                q.append((nx,ny))
def initalized():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

area = 0
for k in range(k):
    r,c = map(int,input().split())
    r-=1
    c-=1

    initalized()

    if can_go(r,c,k):
        visited[r][c]=k
        q.append((r,c))
        bfs(k)
for i in range(n):
    for j in range(n):
        if visited[i][j] != 0:
            area+=1
# print(visited)
print(area)