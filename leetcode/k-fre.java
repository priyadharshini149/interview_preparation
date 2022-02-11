class Solution {
 
    public int[] topKFrequent(int[] nums, int k) {
        HashMap <Integer,Integer> hm=new HashMap <Integer,Integer>();
        Queue <Integer> q=new PriorityQueue<Integer>(Comparator.reverseOrder());
        int m=0;
        int[] h=new int[k];
        for(int i=0;i<nums.length;i++)
        {
            if(hm.containsKey(nums[i]))
            {
                hm.put(nums[i],hm.get(nums[i])+1);
            }
            else
            {
                hm.put(nums[i],1);
            }
        }
        while(m<k){
       
           h[m++]=hm.keySet();}
       
         
      System.out.print(hm);
        return h;
    }
}