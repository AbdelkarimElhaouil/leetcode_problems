# 23. Merge k Sorted Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        def merge(l1: ListNode, l2: ListNode):
            if not l1:
                return l2
            elif not l2:
                return l1
            else:
                head = None
                if l1.val < l2.val:
                    head = l1
                    head.next = merge(l1.next, l2)
                else:
                    head = l2
                    head.next = merge(l1, l2.next)
                return head
    
        if not lists:
            return None
        lst_len = len(lists)
        if  lst_len <= 1:
            return lists[0]
        
        else:
            l1 = self.mergeKLists(lists[:lst_len // 2])
            l2 = self.mergeKLists(lists[lst_len // 2:])
            return merge(l2, l1) 