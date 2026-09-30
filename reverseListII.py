# 92. Reverse Linked List II

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        if left == right:
            return head
        
        cur = head
        left_link = head
        left_node = head
        prev = None
        i = 1
        while i <= right:
            if i == left - 1:
                left_link = cur
                left_node = cur.next
                cur = cur.next
            elif i >= left:
                h = cur
                cur = cur.next
                h.next = prev
                prev = h
            else:
                cur = cur.next
            i += 1
        
        if head == left_node:
            head = prev
        else:
            left_link.next = prev
        
        left_node.next = cur
    
        return head

