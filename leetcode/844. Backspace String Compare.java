class Solution {
    public boolean backspaceCompare(String s, String t) {
        Stack<Character> st1=new Stack<Character>();
        Stack<Character> st2=new Stack<Character>();
        
        for(int i=0;i<s.length();i++)
        {
            if(s.charAt(i)!='#')
            {
                st1.push(s.charAt(i));
            }
            if(s.charAt(i)=='#' && st1.empty() == false){
                st1.pop();
            }
        }
        for(int i=0;i<t.length();i++)
        {
            if(t.charAt(i)!='#')
            {
                st2.push(t.charAt(i));
            }
               if(t.charAt(i)=='#' && st2.empty() == false){
                st2.pop();
            }
        }
        System.out.print(st1);
          System.out.print(st2);
    while (st1.empty() == false &&  st2.empty() == false) {
        
        if (st1.peek() == st2.peek()) {
           
            st1.pop();
            st2.pop();
        }
        else {
           
            return false;
           
        }
    }
        if(st1.empty() == false || st2.empty() == false)
        {
            return false;
        }
        return true;
    }
}