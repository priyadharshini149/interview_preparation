# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        start=head
        fast=head
        while(fast!=None  and fast.next!=None):
            start=start.next
            fast=fast.next.next
            if(start==fast):
                return True
        return False
        