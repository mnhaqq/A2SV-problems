def solve():
    n,k = map(int, input().split())
    c=list(map(int, input().split()))

    #find indices of first element
    first=c[0]
    first_indices=[]
    for i in range(n):
        if c[i]==first:
            first_indices.append(i)

    check_first=len(first_indices)
    if first_indices[-1]==n-1 and check_first>=k:
        print("YES")
        return
    elif check_first<k:
        print("NO")
        return
    remaining=c[first_indices[k-1]+1:]
    #find count of last element
    check_last=remaining.count(remaining[-1])

    if check_last<k:
        print("NO")
    else:
        print("YES")
    

t=int(input())
for _ in range(t):
    solve()