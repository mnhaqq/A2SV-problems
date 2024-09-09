class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        maxx = max(nums)
        ans = count = l = 0
        num_subarrays = (len(nums)/2) * (1 + len(nums))

        for r in range(len(nums)):
            if nums[r] == maxx:
                count += 1
            while l <= r and count >= k:
                if nums[l] == maxx:
                    count -= 1
                l += 1
            ans += r - l + 1

        return int(num_subarrays - ans)