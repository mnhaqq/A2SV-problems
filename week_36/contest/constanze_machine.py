def solve():
    s = input()

    if "m" in s or "w" in s:
        print(0)
        return
    
    dp = [0] * (len(s) + 1)
    dp[0] = dp[1] = 1

    for i in range(2, len(s)+1):
        dp[i] = dp[i-1]
        if s[i-2] == s[i-1] == "n" or s[i-2] == s[i-1] == "u":
            dp[i] += dp[i-2] % ((10**9) + 7)
    print(dp[-1] % ((10**9) + 7))

solve()