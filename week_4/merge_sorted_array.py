class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        final=[]
        pointer1=pointer2=0
        while pointer1 < m and pointer2 < n:
            if nums1[pointer1] <= nums2[pointer2]:
                final.append(nums1[pointer1])
                pointer1+=1
            elif nums2[pointer2] < nums1[pointer1]:
                final.append(nums2[pointer2])
                pointer2+=1

        if pointer1>=m:
            final.extend(nums2[pointer2:n])
        if pointer2>=n:
            final.extend(nums1[pointer1:m])
        nums1[:]=final[:]