n = int(input())
grid = []
for _ in range(n):
    grid.append(list(map(int,input().split())))
visited=[
    [False for _ in range(n)] for _ in range(n)
]

def dfs(i,j):
    global cnt
    dxs, dys = [0,0,-1,1],[-1,1,0,0]
    for x,y in zip(dxs,dys):
        nx,ny = x+i, y+j
        if 0<= nx <n and 0<= ny <n :
            if grid[nx][ny] == 1 and visited[nx][ny] == False:
                cnt +=1
                visited[nx][ny] = True
                dfs(nx,ny)
results =[]
for i in range(n):
    for j in range(n):
        if visited[i][j] == False and grid[i][j] == 1:
            visited[i][j] = True
            cnt = 1
            dfs(i,j)
            results.append(cnt)
# results.sort()
# print(len(results),sorted(results))
print(len(results))
for i in sorted(results):
    print(i)