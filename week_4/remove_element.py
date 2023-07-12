class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left=0
        right=len(nums)-1
        while left<right:
            while nums[right]==val and right>0:
                right-=1
            if left>=right:
                break
            if nums[left]==val:
                nums[left], nums[right] = nums[right], nums[left]
            print(nums)
            left+=1
        return len(nums)-nums.count(val)