def countdown(n):
    if n == 0:
        print(0)
        return
    countdown(n-1)
    print(n)

countdown(10)