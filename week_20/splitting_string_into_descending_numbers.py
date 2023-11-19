class Solution:
    def splitString(self, s: str) -> bool:
        def backtrack(prev_num, idx):
            nonlocal check
            if idx == len(s):
                check = True
                return
            for i in range(idx, len(s)):
                if idx == 0 and i == len(s) - 1:
                    break
                if idx == 0:
                    backtrack(int(s[idx:i+1]), i+1)
                elif int(s[idx:i+1]) == prev_num-1:
                    backtrack(int(s[idx:i+1]), i+1)
                else:
                    continue

        check = False
        backtrack(-1, 0)
        return check