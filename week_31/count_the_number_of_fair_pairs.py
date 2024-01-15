class Solution:
    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:
        ans = 0
        nums.sort()

        for i in range(len(nums)):
            #finding upper bound using binary search
            upper_bound = -1
            low, high = i + 1, len(nums) - 1
            while low <= high:
                mid = (low + high) // 2
                
                if nums[mid] + nums[i] <= upper:
                    upper_bound = mid
                    low = mid + 1
                else:
                    high = mid - 1
            
            #finding lower bound using binary search
            lower_bound = -1
            low, high = i + 1, len(nums) - 1
            while low <= high:
                mid = (low + high) // 2

                if nums[mid] + nums[i] >= lower:
                    lower_bound = mid
                    high = mid - 1
                else:
                    low = mid + 1
            
            if upper_bound > 0 and lower_bound > 0:
                ans += upper_bound - lower_bound + 1

        return ans