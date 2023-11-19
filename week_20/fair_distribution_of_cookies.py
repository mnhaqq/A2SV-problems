class Solution:
    def distributeCookies(self, cookies: list[int], k: int) -> int:
        def backtrack(curr_pos):
            nonlocal ans
            if curr_pos >= len(cookies):
                ans = min(ans, max(kids_scores))
                return
            
            for i in range(k):
                kids_scores[i] += cookies[curr_pos]
                if kids_scores[i] < ans:
                    backtrack(curr_pos+1)
                kids_scores[i] -= cookies[curr_pos]

        ans = float("inf")
        kids_scores = [0] * k
        backtrack(0)
        return ans