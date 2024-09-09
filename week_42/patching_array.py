class Solution:
    def minPatches(self, nums: list[int], n: int) -> int:
        p1 = last_patch = p_s = 0
        check = set(nums)
        patches = set()

        while p_s < n:
            while p_s < n and p1 < len(nums) and nums[p1] < last_patch:
                p1 += 1    

            if p1 < len(nums) and p_s + 1 >= nums[p1]:
                p_s += nums[p1]
                p1 += 1
            elif p_s + 1 not in check:
                patches.add(p_s + 1)
                num = p_s + 1
                p_s += num
                last_patch = num

        return len(patches) 
            
