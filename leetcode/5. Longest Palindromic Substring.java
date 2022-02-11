class Solution {
   
    public String longestPalindrome(String s) {
     int n = s.length();
        int maxLength = 0;
        int ansi=0;
        int ansj=0;
     for(int k=0;k<n;k++){ // k is the center(odd,even), i am assuming
         // Assuming k to be odd center
         int i = k-1;
         int j = k+1; // pointer for expanding the string(palindrome)
         while(i>=0 && j<n && s.charAt(i)==s.charAt(j)){
             i--;
             j++;
         }
         i++;j--;
         if(maxLength<j-i+1){
             maxLength = j-i+1;
             ansi = i;
             ansj = j;
         }
         // Assuming k to be even center
         if(k<n-1 && s.charAt(k)==s.charAt(k+1)){
             i = k; // center-1
             j = k+1; // center-2
             while(i>=0 && j<n && s.charAt(i)==s.charAt(j)){
             i--;
             j++;
         }
         i++;j--;
         if(maxLength<j-i+1){
             maxLength = j-i+1;
             ansi = i;
             ansj = j;
         }
             
         }   
     }
        return s.substring(ansi,ansj+1);
 
    }
}