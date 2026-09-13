# 24. Swap Nodes in Pairs

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        else:
            tmp = head.next
            head.next = tmp.next
            tmp.next = head
            head = tmp
            head.next.next = self.swapPairs(head.next.next)
            return head