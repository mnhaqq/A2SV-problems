from collections import defaultdict

def solve():
    n = int(input())
    mat = []
    for _ in range(n):
        mat.append(list(input().split()))
        mat[-1][0] = int(mat[-1][0])
    
    dic = dict()
    for i in range(len(mat)):
        a = "".join(sorted(mat[i][1]))
        if a in dic:
            dic[a] = min(dic[a], mat[i][0])
        else:
            dic[a] = mat[i][0]
    
    ans = []
    if "A" in dic and "B" in dic and "C" in dic:
        ans.append(dic["A"] + dic["B"] + dic["C"])
    if "A" in dic and "BC" in dic:
        ans.append(dic["A"] + dic["BC"])
    if "AB" in dic and "C" in dic:
        ans.append(dic["AB"] + dic["C"])
    if "AB" in dic and "BC" in dic:
        ans.append(dic["AB"] + dic["BC"])
    if "AB" in dic and "AC" in dic:
        ans.append(dic["AB"] + dic["AC"])
    if "AC" in dic and "B" in dic:
        ans.append(dic["AC"] + dic["B"])
    if "AC" in dic and "BC" in dic:
        ans.append(dic["AC"] + dic["BC"])  
    if "ABC" in dic:
        ans.append(dic["ABC"])
    
    if len(ans) == 0:
        print(-1)
        return
    print(min(ans))

    

solve()