class Solution {
    public String countAndSay(int n) {
        if(n==1)
        {
            return "1";
        }
        String temp=countAndSay(n-1);
        int curDig=temp.charAt(0)-'0',count=1;
        StringBuilder ans=new StringBuilder("");
        int len=temp.length();
        for(int i=1;i<len;i++)
        {
            if(temp.charAt(i)-'0'!=curDig)
            {
                ans.append(Integer.toString(count));
                ans.append(Integer.toString(curDig));
                curDig=temp.charAt(i)-'0';
                count=1;
            }
            else
            {
                count++;
            }
            
        }
        ans.append(count);
        ans.append(curDig);
        
        return ans.toString();
    }
}