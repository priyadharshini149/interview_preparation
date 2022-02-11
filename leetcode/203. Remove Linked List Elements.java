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
    public ListNode removeElements(ListNode head, int val) {
       while(head!=null &&head.val==val)
       {
           head=head.next;
       }
        ListNode h=head;
        while(h!=null && h.next!=null)
        {
            if(h.next.val==val){
                h.next=h.next.next;
            }
            else
            {
                h=h.next;
            }
        }
        
        return head;
        
        
    }
}


