n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

pointer_a = pointer_b = 0
final = []
while pointer_a < n and pointer_b < m:
    if a[pointer_a] <= b[pointer_b]:
        final.append(a[pointer_a])
        pointer_a+=1
    elif b[pointer_b] < a[pointer_a]:
        final.append(b[pointer_b])
        pointer_b+=1

    if pointer_a >= n:
        final.extend(b[pointer_b:m])
    if pointer_b >= m:
        final.extend(a[pointer_a:n])
print(*final)
