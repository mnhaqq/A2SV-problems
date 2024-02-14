class Solution:
    def maxSatisfaction(self, satisfaction: list[int]) -> int:
        satisfaction.sort(reverse=True)
        
        ans = r_s = ltc = 0

        for i in range(len(satisfaction)):
            ltc += r_s + satisfaction[i]
            r_s += satisfaction[i]
            ans = max(ans, ltc)
    
        return ans