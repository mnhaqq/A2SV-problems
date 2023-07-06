class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = nums1+nums2
        arr.sort()
        n = len(arr)
        if n % 2 != 0:
            return arr[n//2]
        else:
            return (arr[n//2]+arr[(n//2)-1])/2