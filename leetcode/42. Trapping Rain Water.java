class Solution {
    public int trap(int[] height) {
       int n=height.length,i,l;
        int[] left=new int[n];
        int[] right=new int[n];
        
        
        left[0]=height[0];
        for(i=1;i<n;i++)
        {
            left[i]=Math.max(left[i-1],height[i]);
        }
        for(i=0;i<n;i++)
        {
            System.out.print(left[i]);
        }
        System.out.print("\n");
        
        
          right[n-1]=height[n-1];
        for(i=n-2;i>=0;i--)
        {
            right[i]=Math.max(right[i+1],height[i]);
        }
        for(i=0;i<n;i++)
        {
            System.out.print(right[i]);
        }
        
        
        int ans=0;
        for(i=1;i<n-1;i++)
        {
            ans+=Math.max(0,Math.min(left[i-1],right[i+1])-height[i]);
        }
        return ans;
    }
}