from collections import deque

class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        dic = dict()

        for num in nums1:
            dic[num] = -1
        
        stack = deque()
        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                dic[stack[-1]] = nums2[i]
                stack.pop()
            if nums2[i] in dic:
                stack.append(nums2[i])

        ans = []
        for i in range(len(nums1)):
            ans.append(dic[nums1[i]])
        return ans