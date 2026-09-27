# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesLen(self, head: ListNode | None) -> int:
        c = 0
        while head:
            c += 1
            head = head.next
        return c

    def reverseLL(self, head: ListNode | None, k: int) -> ListNode | None:
        if k - 1 == 0:
            return head
        new_head = self.reverseLL(head.next, k - 1)
        head.next.next = head
        head.next = None
        return new_head

    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        ll_len = self.nodesLen(head)
        rem = ll_len // k
        if ll_len < k or k == 1:
            return head
        def reverseGroups(head: ListNode | None, rem: int) -> ListNode | None:
            if rem == 0:
                return head
            last_head = head
            nxt_grp = head
            i = 0
            while k > i:
                nxt_grp = nxt_grp.next
                i += 1
            new_head = self.reverseLL(head, k)
            last_head.next = reverseGroups(nxt_grp, rem - 1)
            return new_head
        
        return reverseGroups(head, rem)
