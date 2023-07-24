class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n=len(nums)
        nums.sort()
        final_sum=float("inf")
        i=0
        while i < n:
            l=i+1
            r=n-1
            while l<r:
                if l==i:
                    l+=1
                    continue
                elif r==i:
                    r-=1
                    continue
                check=nums[i]+nums[r]+nums[l]
                if check<=target:
                    if abs(check-target)<abs(final_sum-target):
                        final_sum=check
                    l+=1
                else:
                    if  abs(check-target)<abs(final_sum-target):
                        final_sum=check
                    r-=1             
            i+=1
        return final_sum