# 142. Linked List Cycle II
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        hash_table = set()
        while head:
            if head not in hash_table:
                hash_table.add(head)
            else:
                return head
            head = head.next
        return None