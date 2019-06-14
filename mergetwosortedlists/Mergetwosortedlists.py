# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        prev = dummy = ListNode(None)
        while l1 and l2:
            if l1.val < l2.val:
                prev.next = l1
                l1 = l1.next
            else: 
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        prev.next = l1 or l2
        return dummy.next
        
'''
Runtime: 36 ms, faster than 97.82% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 13.2 MB, less than 35.93% of Python3 online submissions for Merge Two Sorted Lists.

'''
