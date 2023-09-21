# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        #keep track of the end of the previous group
        #at beginning end of the previous group is the dummy node
        prev_grp = dummy

        while True:
            #find the kth node which is the end of the group being reversed
            curr, tmp = prev_grp, 0
            while curr and tmp < k:
                curr = curr.next
                tmp += 1
            node_k = curr
            if not node_k:
                break

            #keep track of the beginning of the next group
            next_grp = node_k.next

            #reverse the current group which is from prev_grp's next to node_k
            #code below is just the normal reversing of linked lists
            prev, curr = node_k.next, prev_grp.next
            while curr != next_grp:
                _next = curr.next
                curr.next = prev
                prev = curr
                curr = _next

            #after reversing some links have to be fixed
            _next = prev_grp.next
            #set prev_grp to point to the node_k which is now the beginning of the
            # reversed portion
            prev_grp.next = node_k
            prev_grp = _next

        return dummy.next