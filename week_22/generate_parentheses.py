class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def backtrack(n_open, n_close, curr):
            if n_open > n or n_close > n_open:
                return
            if n_open == n_close == n:
                result.append(curr)
                return
            
            backtrack(n_open + 1, n_close, curr + "(")
            backtrack(n_open, n_close + 1, curr + ")")

        result = []
        backtrack(0, 0, "")
        return result       