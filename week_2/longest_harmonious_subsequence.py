def solve(nums):
    minimum = min(nums)
    maximum = max(nums)
    tmp = sorted(nums)
    check = False
    for i in range(len(tmp)-1):
        if tmp[i]+1 == tmp[i+1]:
            check = True
    if not check:
        return 0
    
    if minimum < 0:
        status = False
        counter = [0] * (maximum+abs(minimum)+1)
    else:
        status = True
        counter = [0] * (maximum-minimum+2)
    minimum = abs(min(nums))

    for num in nums:
        if status == True:
            counter[num-minimum]+=1
        else:
            counter[num+minimum]+=1

    longest = 0
    if len(nums) <= 1:
        return 0

    for i in range(len(counter)-1):
        if counter[i] != 0 and counter[i+1] != 0:
            longest = max(longest, counter[i]+counter[i+1])
    return longest
