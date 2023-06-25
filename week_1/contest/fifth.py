def solve():
    n, m = map(int, input().split())
    matrix = []
    for i in range(n):
        row = input()
        row = " ".join(row)
        row = row.split()
        matrix.append(row)

    for row in range(n-2,-1,-1):
        for column in range(m):
            if matrix[row][column] == "*":
                i = 1
                status = False
                while row+i < n:
                    if matrix[row+i][column] != ".":
                        break
                    else:
                        status=True
                    i+=1
                if status == True:    
                    matrix[row+i-1][column] = "*"
                    matrix[row][column] = "."

    for row in matrix:
        print("".join(row))




t = int(input())
for _ in range(t):
    solve()