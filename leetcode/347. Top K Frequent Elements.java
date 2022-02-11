class Solution {
 
    public int[] topKFrequent(int[] nums, int k) {
        HashMap <Integer,Integer> hm=new HashMap <Integer,Integer>();
       
         PriorityQueue<Integer> q = new PriorityQueue<>((a,b) -> (hm.get(b)-hm.get(a)));
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
        for(Integer r:hm.keySet()){
            q.add(r);
        }
       for(int i=0;i<k;i++)
       {
           h[i]=q.poll();
       }
         
      System.out.print(hm);
        return h;
    }
}
