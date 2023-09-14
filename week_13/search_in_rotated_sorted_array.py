class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #use binary search to find minimum element
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
                min_index = mid
        
        #perform binary search on left side
        low, high = 0, min_index
        while low <= high:
            mid = (high+low) // 2
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                return mid
        
        #perform binary search on right side
        low, high = min_index, len(nums)-1
        while low <= high:
            mid = (high+low)//2
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                return mid
        return -1