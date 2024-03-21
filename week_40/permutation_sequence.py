class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def backtrack():
            if len(check) == n:
                res.append(check[:])
                return

            if len(res) == k:
                return

            for i in range(1, n+1):
                if i not in check:
                    check.append(i)
                    backtrack()
                    check.pop()

        res = []
        check = []
        backtrack()
        res[-1] = map(str, res[-1])
        return ''.join(res[-1])
