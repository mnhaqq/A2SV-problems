n, k = map(int, input().split())
theorems_taught = list(map(int, input().split()))
behaviors = list(map(int, input().split()))

# calculate number of theorems taught when student was awake already
awake = 0
for index, behavior in enumerate(behaviors):
    if behavior == 1:
        awake+=theorems_taught[index]

gain = 0
for i in range(k):
    if behaviors[i] == 0:
        gain+=theorems_taught[i]

max_theorems = awake + gain


for i in range(1, n-k+1):
    if behaviors[i+k-1] == 0:
        gain+=theorems_taught[i+k-1]
    if behaviors[i-1] == 0:
        gain-=theorems_taught[i-1]
    max_theorems=max(max_theorems, awake+gain)

print(max_theorems)