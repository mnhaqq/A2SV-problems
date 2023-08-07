class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        answer=[]
        left_sum=0
        right_sum=sum(nums[1:])
        answer.append(abs(right_sum-left_sum))
        for i in range(len(nums)-1):
            left_sum+=nums[i]
            right_sum-=nums[i+1]
            answer.append(abs(right_sum-left_sum))
        return answer