# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    
    # Going through LinkedList and returning an Integer
    def linked_to_int(self, node: ListNode) -> int:
        data = ''
        current = node
        # if the current node is not null continue on
        while current != None:
            data += str(current.val)
            current = current.next
        return int(data)
    
    def int_to_linked(self, number: int) -> ListNode:
        # return head of LinkedList
        number = str(number)[::-1]
        current = None
        for i in range(len(number)):
            if current == None:
                current = ListNode(int(number[i]))
            elif current != None:
                current.next = ListNode(number[i])
                current = current.next
        return current
            
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum = self.linked_to_int(l1) + self.linked_to_int(l2)
        return self.int_to_linked(sum)
    '''
    Took 48 ms
    '''
