class Solution:
    def minDifference(self, nums: list[int]) -> int:
        if len(nums) <= 4:
            return 0

        nums.sort()
        ans = []
        ans.append(nums[-1] - nums[3])
        ans.append(nums[-2] - nums[2])
        ans.append(nums[-3] - nums[1])
        ans.append(nums[-4] - nums[0])

        return min(ans)