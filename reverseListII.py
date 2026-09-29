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
        tail = head
        prev = None
        i = 1
        while i <= right:
            if i == left - 1:
                left_link = cur
                tail = cur.next
                cur = cur.next
            elif i >= left:
                h = cur
                cur = cur.next
                h.next = prev
                prev = h
            i += 1
        
        if head == tail:
            head = prev
        else:
            left_link.next = prev
            tail.next = cur
    
        return head

