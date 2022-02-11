/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode prev=head,cur=head;
        int l=0;
        while(cur!=null)
        {
            l++;
            cur=cur.next;
        }
        int tar=l-n-1;
        cur=head.next;
        if(cur==null){
            cur=head;
            head=null;
            return head;
        }
        if(n==l)
        {
            head=head.next;
        }
        while(tar>0 &&cur!=null)
        {
            prev=prev.next;
            cur=cur.next;
            
        tar--;
        }
        prev.next=cur.next;
        System.out.print(prev.val);
         System.out.print(cur.val);
        return(head);
    }
}