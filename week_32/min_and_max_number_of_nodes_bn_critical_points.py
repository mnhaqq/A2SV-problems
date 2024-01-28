from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> list[int]:
        min_dist = max_dist = -1
        cr_pt = first = -1

        prev = head
        ptr = head.next
        _next = ptr.next
        
        i = 1
        while _next:
            if prev.val > ptr.val < _next.val or prev.val < ptr.val > _next.val:
                if min_dist == -1:
                    if cr_pt == -1:
                        first = max(first, i)
                        cr_pt = i
                    else:
                        min_dist = (i - cr_pt)
                else:
                    min_dist = min(min_dist, i - cr_pt)
                cr_pt = i
            i += 1
            prev, ptr, _next = ptr, _next, _next.next
        if min_dist > -1:
            max_dist = cr_pt - first
        return [min_dist, max_dist]
        
        