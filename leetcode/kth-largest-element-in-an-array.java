class Solution 
{
    public int findKthLargest(int[] nums, int k) 
    {
        	Queue<Integer> qu=new PriorityQueue<>();
            for(int i=0;i<nums.length;i++)
           { 
             if(qu.size()<k)
             {
                 qu.offer(nums[i]);
                 
             }
             else
             {if(qu.peek()<nums[i])
                 {
                     qu.poll();
                     qu.offer(nums[i]);
                 }
             }
                
           }
        
        return(qu.peek());
    }
}