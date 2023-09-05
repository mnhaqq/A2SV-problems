class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
        
        pr_sum = [0] * (len(nums)+1)
        for i in range(1, len(pr_sum)):
            pr_sum[i] = pr_sum[i-1] + nums[i-1]
        
        count = 0
        dic = dict()
        for i in range(len(pr_sum)):
            if pr_sum[i] - k in dic:
                count += dic.get(pr_sum[i]-k)
            dic[pr_sum[i]] = dic.get(pr_sum[i],0) + 1
        return count