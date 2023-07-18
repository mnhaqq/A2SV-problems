def check_beauty(matrix):
    #check row
    for i in range(2):
        if matrix[i][0] > matrix[i][1]:
            return False

    #check columns
    for i in range(2):
        if matrix[0][i] > matrix[1][i]:
            return False
    return True

def rotate_matrix(matrix):
    matrix[0][0], matrix[1][0] = matrix[1][0], matrix[0][0]
    matrix[0][1], matrix[1][0] = matrix[1][0], matrix[0][1]
    matrix[1][0], matrix[1][1] = matrix[1][1], matrix[1][0]

def solve():
    matrix=[]
    for i in range(2):
        tmp=list(map(int, input().split()))
        matrix.append(tmp)
    for i in range(4):
        if check_beauty(matrix):
            print("YES")
            return
        rotate_matrix(matrix)
    print("NO")


t=int(input())
for _ in range(t):
    solve()