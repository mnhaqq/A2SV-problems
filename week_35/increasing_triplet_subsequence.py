class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        if len(nums) < 3:
            return False

        first = second = float("inf")
        
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False