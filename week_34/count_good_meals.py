class Solution:
    def countPairs(self, deliciousness: list[int]) -> int:
        dic = dict()
        ans = 0

        for i in range(len(deliciousness)):
            j = 0
            while j < 22:
                if ((2**j) - deliciousness[i]) in dic:
                    ans += dic[((2**j) - deliciousness[i])]
                j += 1
            if deliciousness[i] in dic:
                dic[deliciousness[i]] += 1
            else:
                dic[deliciousness[i]] = 1
        return ans % (10**9 + 7)