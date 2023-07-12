class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        targets=[]
        for i in range(len(nums)-1):
            if nums[i]==key:
                targets.append(nums[i+1])
        counter=[0]*(max(targets)+1)
        for i in range(len(targets)):
            counter[targets[i]]+=1
        
        return counter.index(max(counter))