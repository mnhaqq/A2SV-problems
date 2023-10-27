
def solve():
    a = input()
    b = input()
 
    dic = dict()
    def check(s1, s2):
        if s1 == s2:
            return True
        if len(s1) % 2 == 1 or len(s2) % 2 == 1:
            return False
        if (s1, s2) in dic:
            return dic[s1, s2]

        s1_p1 = s1[:len(s1)//2]
        s1_p2 = s1[len(s1)//2:]
        s2_p1 = s2[:len(s2)//2]
        s2_p2 = s2[len(s2)//2:]
 
        dic[s1, s2] = (check(s1_p1, s2_p1) and check(s1_p2, s2_p2)) or (check(s1_p1, s2_p2) and check(s1_p2, s2_p1))
        
        return dic[s1, s2]
    
    ans = check(a, b)
    if ans:
        print("YES")
    else:
        print("NO")
 
solve()