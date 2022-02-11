# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        res=[]
        for i in lists:
            lis=i
            while(lis!=None):
                res.append(lis.val)
                lis=lis.next
                
        res.sort()
        h=None
        h1=None
        for i in res:
            n=ListNode(i)
            if(h==None):
                h=n
                h1=n
            else:
                h1.next=n
                h1=h1.next
        return h
       