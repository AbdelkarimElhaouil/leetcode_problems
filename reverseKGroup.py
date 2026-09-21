# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesLen(self, head: ListNode | None) -> int:
        if not head:
            return 0
        return 1 + head.next

    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:     
        nodes_len = self.nodesLen(head)

        def reverseGroup(head: ListNode | None, prev: ListNode | None, k: int) -> ListNode:
            if k == 1:
                head.next = prev
                return head
            tmp = head.next
            head.next = prev
            return reverseGroup(head, tmp, k - 1)
        
        if nodes_len > k == 0:
            return head


        
        
