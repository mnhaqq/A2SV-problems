t = int(input())
maxx = 2 * (10**5)
p_s = [0] * (maxx + 1)

for i in range(1, maxx + 1):
    num = sum(int(digit) for digit in str(i))
    p_s[i] = p_s[i - 1] + num
    
for _ in range(t):
    n = int(input())
    print(p_s[n])