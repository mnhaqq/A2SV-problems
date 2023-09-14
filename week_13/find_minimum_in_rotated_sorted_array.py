class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_element = float("inf")
        min_index = -1
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (high + low) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid - 1
            if nums[mid] < min_element:
                min_element = nums[mid]
        return min_element