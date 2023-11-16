from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(list1, list2):
            p1 = list1
            p2 = list2

            dummy = ListNode(0)
            ptr = dummy
            while p1 and p2:
                if p1.val <= p2.val:
                    ptr.next = p1
                    p1 = p1.next
                    ptr = ptr.next

                else:
                    ptr.next = p2
                    p2 = p2.next
                    ptr = ptr.next

            if p1:
                ptr.next = p1
            elif p2:
                ptr.next = p2

            return dummy.next

        def sort(head):
            if not head or not head.next:
                return head
            
            slow = fast = prev = head
            while fast:
                prev = slow
                slow = slow.next
                fast = fast.next
                if fast:
                    fast = fast.next
            prev.next = None
            
            list1 = sort(head)
            list2 = sort(slow)
            return merge(list1, list2)

        dummy = ListNode(0)
        if not lists:
            return dummy.next
        prev = dummy
        for i in range(len(lists)):
            head = lists[i]
            ptr = head
            while ptr:
                prev.next = ptr
                prev = ptr
                ptr = ptr.next
        ptr = dummy
        while ptr:
            ptr = ptr.next
            
        ans = sort(dummy.next)
        return ans