class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        def backtrack(idx):
            nonlocal curr_sum
            if curr_sum == target:
                ans.append(curr[:])
                return

            for i in range(idx, len(candidates)):
                if (curr_sum + candidates[i]) > target:
                    return
                curr_sum += candidates[i]
                curr.append(candidates[i])
                backtrack(i)
                curr_sum -= candidates[i]
                curr.pop()
                
        candidates.sort()
        ans = []
        curr = []
        curr_sum = 0
        backtrack(0)
        return ans