class Solution {
    public boolean isValid(String s) {
        Stack <Character>st=new Stack<Character>();
        for (int i=0;i<s.length();i++)
        {
            if(s.charAt(i)=='('||s.charAt(i)=='['||s.charAt(i)=='{')
            {
                st.push(s.charAt(i));
            }
            else{
                if(st.empty()){
                    return false;
                }
                else
                {
                    char t=st.pop();
                        if(t=='(' && s.charAt(i)!=')')
                        {
                            return false;
                        }
                        if(t=='[' && s.charAt(i)!=']')
                        {
                            return false;
                        }
                        if(t=='{' && s.charAt(i)!='}')
                        {
                            return false;
                        }
                }
            }
        }
        
        
        if(st.empty())
        {
            return true;
        }
        return false;
        
        
        
    }
}