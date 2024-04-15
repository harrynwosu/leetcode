# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeNodes(self, head):
        '''
        Create dummy node and simulate the problem, building the required list starting from dummy
        Keep track of a sum variable an if we encounter a zero, create a new node with the current sum as its val then reset the sum to 0
        main pointer here tracks our original linked list, curr tracks the one we are building
        '''
        curr_sum = 0
        main, dummy = head.next, ListNode(0)
        curr = dummy

        while main:
            curr_sum += main.val

            if main.val == 0:
                curr.next = ListNode(curr_sum)
                curr = curr.next
                curr_sum = 0
            
            main = main.next
        
        return dummy.next