bool isPalindrome(int x){
int dig=0,n=x;
    double rev=0;
    if(x<0)
    {
        return false;
    }
    
    while(x>0){
        dig=x%10;
        rev=(rev*10)+dig;
        x/=10;
    }
  return rev==n;
    
}