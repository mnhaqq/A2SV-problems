class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        dic=Counter(nums[:k])
        ans=0
        maximum=sum(nums[:k])
        if len(dic)==k:
            ans=maximum
        l=0
        r=k
        while r<len(nums):
            maximum+=nums[r]
            maximum-=nums[l]
            dic[nums[r]]=dic.get(nums[r],0)+1
            dic[nums[l]]-=1
            if dic.get(nums[l])==0:
                del dic[nums[l]]

            if len(dic)==k:
                ans=max(maximum,ans)
            l+=1
            r+=1
        return ans