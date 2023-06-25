n, m = map(int, input().split())

matrix = []
for _ in range(n):
    row = list(input())
    matrix.append(row)

check_matrix = []
#check rows
for row in matrix:
    check = []
    dic = dict()
    for element in row:
        check.append(element)
    for element in check:
        dic[element] = dic.get(element, 0) + 1

    for i in range(len(check)):
        if dic[check[i]] > 1:
            check[i] = 0
    check_matrix.append(check)

z = 0
final = ""
#check columns
for i in range(m):
    check = []
    dic = dict()
    for j in range(n):
        check.append(matrix[j][i])

    for element in check:
        dic[element] = dic.get(element, 0) + 1

    for i in range(len(check)):
        if dic[check[i]] > 1:
            check[i] = 0

    for k in range(len(check)):
        if check_matrix[k][z] != 0:
            check_matrix[k][z] = check[k]
    z+=1

for row in check_matrix:
    for element in row:
        if element != 0:
            final+=element
print(final)