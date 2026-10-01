# 142. Linked List Cycle II

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