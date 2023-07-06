def solve():
    n = int(input())

    if n%2 == 0:
        print(-1)
        return
    else:
        binary = bin(n)
        binary = binary[2:-1]
        binary = " ".join(binary)
        binary = binary.split()
        for i in range(len(binary)):
            binary[i] = int(binary[i])+1
        print(len(binary))
        print(*binary)
        

t = int(input())
for _ in range(t):
    solve()