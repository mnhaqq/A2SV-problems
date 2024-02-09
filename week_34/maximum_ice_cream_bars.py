class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        counter = [0] * (max(costs) + 1)
        
        for i in range(len(costs)):
            counter[costs[i]] += 1

        ans = spent = 0
        for i in range(len(counter)):
            while counter[i] > 0 and (spent + i) <= coins:
                ans += 1
                spent += i
                counter[i] -= 1
        return ans
