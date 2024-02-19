class Solution:
    def partitionArray(self, nums: list[int], k: int) -> int:
        nums.sort()

        ans = 1
        mini = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - mini > k:
                ans += 1
                mini = nums[i]
        return ans