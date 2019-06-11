# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
           l1, l12, l13 = str(l1.val), str(l1.next.val), str(l1.next.next.val)
           l2, l22, l23 = str(l2.val), str(l2.next.val), str(l2.next.next.val)
           l1 = int(l13 + l12 + l1)
           l2 = int(l23 + l22 + l2)
           sum = str(l1 + l2)[::-1]
           l3 = ListNode(sum[0])
           l3.next = ListNode(sum[1])
           l3.next.next = ListNode(sum[2])
           return l3
           
