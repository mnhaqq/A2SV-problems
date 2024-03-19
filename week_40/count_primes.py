class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        arr = [True] * (n)
        arr[0] = arr[1] = False
        i = 2
        while (i ** 2 < n):
            if not arr[i]:
                i += 1
                continue
            for j in range(i*2, n, i):
                arr[j] = False
            i += 1
        return sum(arr)
