class Solution:
    def count(self, nums, mid):
        count = 0
        for num in nums:
            if num <= mid:
                count += 1
        if count > mid:
            return True
        return False
        
    def findDuplicate(self, nums: List[int]) -> int:
        low, high = 1, max(nums)
        ans = 0
        while low <= high:
            mid = (low+high)//2
            if self.count(nums, mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans