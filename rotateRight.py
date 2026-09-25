# 61. Rotate List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        def NodesLen(head: ListNode | None):
            if not head:
                return 0
            return 1 + NodesLen(head.next)
    
        if not head or not head.next:
            return head
    
        nodes_len = NodesLen(head)
        rem = k if nodes_len > k else k % nodes_len 
        if not rem:
            return head
    
        i = 0
        last_head = head
        while head.next:
            if i == nodes_len - rem - 1:
                tail = head
                new_head = head.next
            i += 1
            head = head.next
        
        head.next = last_head
        tail.next = None
        return new_head