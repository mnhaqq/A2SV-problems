class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        dic = dict()
        count = 0
        for i in range(len(time)):
            time[i] = time[i] % 60
        for i in range(len(time)):
            if (60-time[i]) % 60 in dic:
                count+=dic[(60-time[i]) % 60]
            dic[time[i]] = dic.get(time[i], 0) + 1
        return count