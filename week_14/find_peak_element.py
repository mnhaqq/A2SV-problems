class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums.append(float("-inf"))
        low, high = 0, len(nums)-1

        while low <= high:
            mid = (high + low) // 2
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid] < nums[mid+1] and nums[mid] > nums[mid-1]:
                low = mid + 1
            else:
                high = mid - 1
        return high