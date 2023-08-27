input_string = input()
n = len(input_string)
l = r = 0
out = []
while r < n:
    if input_string[r] != input_string[l]:
        out.append(input_string[l])
        out.append(str(r-l))
        l = r
    r+=1
out.append(input_string[l])
out.append(str(r-l))
out = "".join(out)
print(out)
