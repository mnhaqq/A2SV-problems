class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        def backtrack(curr, idx):
            if len(curr) == len(digits):
                if curr:
                    result.append(curr)
                return

            for i in dic[digits[idx]]:
                backtrack(curr + i, idx + 1)
        
        dic = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno",
               '7':"pqrs", '8':"tuv", '9':"wxyz"}

        result = []
        backtrack("", 0)
        return result