from collections import deque

q= deque()

n, m = map(int,input().split())
grid= [
    list(map(int,input().split()))
    for _ in range(n)
]

visited = [
    [False for _ in range(m)] for _ in range(n)
]

def in_range(i,j):
    return 0<=i<n and 0<=j<m
def can_go(i,j):
    if not in_range(i,j): return False
    if visited[i][j]: return False
    if grid[i][j] == 0: return False
    return True

def bfs():
    global exit
    while q:
        x,y = q.popleft()
        dxs,dys = [0,0,1,-1],[1,-1,0,0]
        for dx,dy in zip(dxs,dys):
            nx = dx+x
            ny = dy+y
            if nx == (n-1) and ny ==(m-1):
                exit = 1
                return 1
            if can_go(nx,ny):
                visited[nx][ny] =True
                q.append((nx,ny))

exit = 0
q.append((0,0))
bfs()

print(exit)