from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> list[int]:
        ans = []
        stack = []
        
        i = 0
        ptr = head
        while ptr:
            ans.append(0)
            while stack and ptr.val > stack[-1][1]:
                ans[stack[-1][0]] = ptr.val
                stack.pop()
            stack.append([i, ptr.val])
            ptr = ptr.next
            i += 1
        return ans

        