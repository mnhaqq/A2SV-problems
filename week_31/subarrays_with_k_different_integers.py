class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
    
        def find_subarrays(n):
            ans = l = 0
            count = dict()

            for r in range(len(nums)):
                if nums[r] not in count:
                    count[nums[r]] = 1
                else:
                    count[nums[r]] += 1

                while l <= r and len(count) > n:
                    count[nums[l]] -= 1
                    if count[nums[l]] == 0:
                        del count[nums[l]]
                    l += 1
                ans += (r - l + 1)
            return ans

        return find_subarrays(k) - find_subarrays(k-1)
                
                    