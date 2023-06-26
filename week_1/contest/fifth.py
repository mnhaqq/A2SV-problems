def solve():
    # take size of the matrix
    n, m = map(int, input().split())
    matrix = []
    #take rows of matrix and convert them from string to array
    for i in range(n):
        row = input()
        row = " ".join(row)
        row = row.split()
        matrix.append(row)

    # iterate through rows from bottom to top
    # start from last but one row
    for row in range(n-2,-1,-1):
        # for each row iterate through each column
        for column in range(m):
            #check if current position is a stone
            if matrix[row][column] == "*":
                i = 1
                # status checks if cells below contain empty cells
                status = False
                # while loop to check whether rows below contain empty cells
                while row+i < n:
                    # if obstacle or another stone is reached
                    # break out of the loop since we cant go further below
                    if matrix[row+i][column] != ".":
                        break
                    # else if empty cell available set status to true
                    else:
                        status=True
                    i+=1
                # if status is true after we break out of the while loop
                # it means that at least one empty cell is below out stone
                if status == True:    
                    # swap stone with empty cell
                    matrix[row+i-1][column] = "*"
                    matrix[row][column] = "."

    # print simulated grid in form of a string
    for row in matrix:
        print("".join(row))



t = int(input())
for _ in range(t):
    solve()