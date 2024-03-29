def solve():
    s = input()
    hr, m = map(int, s.split(':'))

    if 1 <= hr <= 12:
        ans = s
        if hr == 12:
            ans += ' PM'
        else:
            ans += ' AM'
        print(ans)
        return
    
    if hr == 0:
        ans = '12' + ':' + str(m).zfill(2) + ' AM'
        print(ans)
        return

    hr %= 12
    ans = str(hr).zfill(2) + ':' + str(m).zfill(2) + ' PM'
    print(ans)

t = int(input())
for _ in range(t):
    solve()