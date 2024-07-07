import sys
sys.setrecursionlimit(10000)

n,m = map(int,input().split())
grid= [
    list(map(int,input().split())) for _ in range(n)
]
visited =[
    [False for _ in range(m)]
    for _ in range(n)
]


def initalized_visited():
    for i in range(n):
        for j in range(m):
            visited[i][j] = False

def in_range(i, j):
    return 0 <= i < n and 0 <= j < m

def can_go(i, j, k):
    if not in_range(i, j): return False
    if visited[i][j]: return False
    if grid[i][j] <= k: return False
    return True

def dfs(i,j,k):
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    for dx,dy in zip(dxs,dys):
        nx,ny = i+dx, j+dy
        if can_go(nx,ny,k):
            visited[nx][ny] = True
            dfs(nx,ny,k)

# k에 따른 영역 개수
def get_area(k):
    initalized_visited()
    global area 
    area = 0
    for i in range(n):
        for j in range(m):
            if can_go(i,j,k):
                visited[i][j] = True
                area+=1
                dfs(i,j,k) #여기서 한 군집을 거쳐가면 visited를 ture

ans_area, ans_k = 0,1

for k in range(1,101):
    get_area(k)
    if ans_area <= area:
        ans_area = area
        ans_k = k

print(ans_area, ans_k)