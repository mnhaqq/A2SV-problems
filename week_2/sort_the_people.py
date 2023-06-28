
def solve(names, heights):
    """
    out = [0] * len(names)
    reversed_height = sorted(heights, reverse=True)

    dic = dict()
    for i in range(len(names)):
        dic[heights[i]] = names[i]

    for i in range(len(names)):
        out[i] = dic.get(reversed_height[i])
    return out
    """

    # using bubble sort
    for i in range(len(names)):
        swap = False
        for j in range(len(names)-i-1):
            if heights[j] < heights[j+1]:
                swap = True
                heights[j], heights[j+1] = heights[j+1], heights[j]
                names[j], names[j+1] = names[j+1], names[j]
        if not swap:
            break

    return names
    """
    Time complexity is O(n^2)
    """

names = ["Alice","Bob","Bob"]
heights = [155,185,150]
print(solve(names, heights))