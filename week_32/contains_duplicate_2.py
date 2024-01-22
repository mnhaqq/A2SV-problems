class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        dic = dict()
        l = 0

        for r in range(len(nums)):
            while l < r and abs(l - r) > k:
                dic[nums[l]] -= 1
                if dic[nums[l]] == 0:
                    del dic[nums[l]]
                l += 1
            if nums[r] in dic:
                return True
            dic[nums[r]] = 1
        return False