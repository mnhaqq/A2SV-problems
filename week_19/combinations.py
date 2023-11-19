class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        def backtrack(curr):
            if len(curr) == k:
                result.append(curr[:])
                return
            if len(curr) == 0:
                for i in range(1, n+1):
                    curr.append(i)
                    backtrack(curr)
                    curr.pop()
            else:
                for i in range(max(curr)+1, n+1):
                    curr.append(i)
                    backtrack(curr)
                    curr.pop()
        
        result = []
        backtrack([])
        return result