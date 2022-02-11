class Solution {
    public int lengthOfLongestSubstring(String s) {
        int ans=0;int j,i;
        for( i=0;i<s.length();i++)
        {
            int[] freq=new int [256];
            for( j=i;j<s.length();j++)
            {
                
                if(freq[(int)s.charAt(j)]>0)
                {
                    break;
                }
                freq[(int)s.charAt(j)]++;
            }
            ans=Math.max(ans,j-i);
        }
      return ans;  
    }
}