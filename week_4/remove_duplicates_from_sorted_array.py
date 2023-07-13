class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = list(set(nums))
        k = len(unique)
        sorted_portion = []
        holder=seeker=0
        while seeker < len(nums):
            if nums[seeker] not in sorted_portion:
                sorted_portion.append(nums[seeker])
                nums[holder], nums[seeker] = nums[seeker], nums[holder]
            
            while seeker < len(nums) and nums[seeker] in sorted_portion:
                seeker+=1
            holder+=1
        return k