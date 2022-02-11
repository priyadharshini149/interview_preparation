#include <stdio.h>
int swap(int *a,int *b){
    int temp=*a;
    *a=*b;
    *b=temp;
}
int bubble_sort(int a[],int n)
{
    for(int i=0;i<n;i++)
    {for(int j=0;j<n-i-1;j++)
        {
            if(a[j]>a[j+1])
            {swap(&a[j],&a[j+1]);
            }
        }
    }
}

int main()
{
   int n;
   scanf("%d",&n);
   int a[n];
   for(int i=0;i<n;i++)
   {
       scanf("%d",&a[i]);
   }
   bubble_sort(a,n);
   for(int i=0;i<n;i++)
   {
       printf("%d\t",a[i]);
   }

    return 0;
}
