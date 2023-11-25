import sys
def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    matrix = [[0] * n for i in range(n)]
    #row
    for i in range(len(matrix[0])):
        matrix[a[0]][i] = 1 
    #col
    for i in range(len(matrix)):
        matrix[i][a[1]-1] = 1
    #diagonal
    row = n-a[1]
    col = a[0]-1
    x,y = row,col
    while x > 0 and y > -1:
        matrix[x][y] = 1
        x-=1
        y-=1
    x,y = row,col
    while x < n and y < n:
        matrix[x][y] = 1
        x+=1
        y+=1
    x,y = row,col
    while x < n and y > -1:
        matrix[x][y] = 1
        x+=1
        y-=1
    x,y = row,col
    while y < n and x > -1:
        matrix[x][y] = 1
        x-=1
        y+=1

    #place king
    matrix[n-b[1]][b[0]-1] = 2
    #destination
    matrix[n-c[1]][c[0]-1] = 3
    for r in matrix:
        print(r)
    moves = [(-1,-1), (-1,0), (-1,-1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    count = 0
    def dfs(x, y):
        # nonlocal count
        # count += 1
        # if count == 10:
        #     print("yes")
        #     return
        pos = [x,y]
        if pos == matrix[n-c[1]][c[0]-1]:
            return True
        for a, b in moves:
            if matrix[x+a][y+b] == 1:
                continue
            dfs(x+a, y+b)
    if dfs(n-b[1], b[0]-1):
        print("yes")

solve()