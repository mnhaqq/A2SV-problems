class Solution:
    def maxLength(self, arr: list[str]) -> int:
        def backtrack(string, pos):
            nonlocal ans
            s_set = set(string)
            n_set = set(arr[pos])

            if len(s_set.intersection(n_set)) > 0 and len(set(string)) == len(string):
                ans = max(len(s_set), ans)
                return
            if (pos + 1) >= len(arr) and (len(set(string)) + len(set(arr[pos]))) == (len(string) + len(arr[pos])):
                ans = max(len(s_set) + len(arr[pos]), ans)
                return
            
            for i in range(pos + 1, len(arr)):
                backtrack(string + arr[pos], i)
        
        ans = 0
        for i in range(len(arr)):
            backtrack("", i)
        return ans