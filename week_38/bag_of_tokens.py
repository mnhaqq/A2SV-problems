class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()  
        l, r = 0, len(tokens) - 1
        score = tmp = 0
        flag = False

        while l <= r:
            if power >= tokens[l]:
                tmp += 1
                power -= tokens[l] 
                l += 1
                score = max(tmp, score)

            elif tmp >= 1:
                power += tokens[r]
                tmp -= 1
                r -= 1
            else:
                break
        return score
