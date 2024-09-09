class Solution:
    def minimumAddedCoins(self, coins: list[int], target: int) -> int:
        coins.sort()
        ans = i = 0
        missen = 1

        while missen <= target:
            if i < len(coins) and coins[i] <= missen:
                missen += coins[i]
                i += 1
            else:
                missen += missen
                ans += 1
        return ans