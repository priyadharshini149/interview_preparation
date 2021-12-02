int roman(char c)
{
    switch(c)
    {
               case 'I':return 1;
               case 'V':return 5;
               case 'X':return 10;
               case 'L':return 50;
               case 'C':return 100;
               case 'D':return 500;
               case 'M':return 1000;
        default: return 0;
    }
}

int romanToInt(char * s){

    int numb=roman(s[0]);
for(int i=1;s[i]!='\0';i++)
{
    int prev=roman(s[i-1]);
    int cur=roman(s[i]);
    if(prev<cur){
        numb=numb-prev+(cur-prev);
    }
    else
    {
        numb+=cur;
    }
 
}