from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Use a stack to keep track of elements 
        and a variable for  carry-overs when needed
        If after everything, we have a carry over leftover, make it the new head.
        '''
        curr = head
        carry = 0
        stack = []

        while curr:
            stack.append(curr)
            curr = curr.next
        
        while stack:
            curr_node = stack.pop()
            carry, curr_node.val = divmod((curr_node.val * 2) + carry, 10)
        
        if carry:
            head = ListNode(carry)
            head.next = curr_node
        
        return head


    def doubleIt2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        NB: Doesn't work - ValueError: Exceeds the limit (4300 digits) for integer string conversion @ line 42
        Put values in an array, join them and double the concatenated int
        Loop through each digit of the doubled int, while creating a new linked list. (NB: chose to start with a dummy node)
        '''
        curr = head
        vals = [] 

        while curr:
            vals.append(str(curr.val))
            curr = curr.next

        doubled = int("".join(vals)) * 2

        dummy = new_curr = ListNode(0)

        for num in str(doubled):
            new_curr.next = ListNode(int(num))
            new_curr = new_curr.next
        
        return dummy.next
