# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        v=[]
        while(head):
            if(head not in v):
                v.append(head)
                head=head.next
            else:
                return head
        return None