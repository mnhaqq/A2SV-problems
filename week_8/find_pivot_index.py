class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        #create left sums array
        sums=0
        left_sums=[sums]
        for i in range(len(nums)-1):
            sums+=nums[i]
            left_sums.append(sums)
        
        #create right sums array
        sums=sum(nums)-nums[0]
        right_sums=[sums]
        for i in range(len(nums)-1):
            sums-=nums[i+1]
            right_sums.append(sums)

        #look for pivot index
        for pointer in range(len(right_sums)):
            if right_sums[pointer]==left_sums[pointer]:
                return pointer
        return -1