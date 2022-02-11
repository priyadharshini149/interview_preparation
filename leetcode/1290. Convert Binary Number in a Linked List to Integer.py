# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        
        cur=head.next
        n=head.val
        while(cur):
            n=n*10+cur.val
            cur=cur.next
        return(int(str(n),2))
        