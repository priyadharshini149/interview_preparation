class Solution {
    public String largestNumber(int[] nums) {
   int n=nums.length;
        List<String> list=new ArrayList<>();
        for(int i=0;i<n;i++)
        {
            list.add(String.valueOf(nums[i]));
            
        }
        Comparator<String> comp=new Comparator<>()
        {
            public int compare(String a,String b)
            {
                String case1=a+b;
                String case2=b+a;
                    return case2.compareTo(case1);
                
            }
                
        };
        Collections.sort(list,comp);
            String ans="";
        for(String s:list)
        {
            ans=ans+s;
        }
        if(ans.charAt(0)=='0')
        {
            return "0";
        }
        return ans;
    }
}