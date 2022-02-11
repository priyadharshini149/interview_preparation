# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
       
        h=None
        h1=None
        cur=head
        odd=1
        while(cur):
            if(odd%2!=0):
                n=ListNode(cur.val)
                if(h==None):
                    h=n
                    h1=n
                else:
                    h1.next=n
                    h1=h1.next
           
            odd+=1
            cur=cur.next
        even=1
        cur=head
        while(cur):
            if(even%2==0):
                
                n=ListNode(cur.val)
                if(h==None):
                    h=n
                    h1=n
                else:
                    h1.next=n
                    h1=h1.next
           
            even+=1
            cur=cur.next
        return(h)