from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Use a monotonic stack to ensure that node vals are non-increasing
        How: Add nodes to the stack, once you encounter a node value greater than the top val, continue popping until the top node in the stack are greater than or equal to the current or the stack becomes empty.
        Build the new linked list from the nodes left in the stack
        '''
        curr = head
        stack = []

        while curr:
            while stack and stack[-1].val < curr.val:
                stack.pop()

            stack.append(curr)
            curr = curr.next
        
        new_head = new_curr = stack[0]

        for i in range(1, len(stack)):
            new_curr.next = stack[i]
            new_curr = new_curr.next
        
        return new_head


        