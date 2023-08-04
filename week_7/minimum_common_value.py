class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums1=set(nums1)
        nums2=set(nums2)
        nums=nums1.intersection(nums2)
        if len(nums)<1:
            return -1
        return min(nums)