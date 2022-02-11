#include <stdio.h>
int swap(int *a,int *b){
    int temp=*a;
    *a=*b;
    *b=temp;
}
int selection_sort(int a[],int n)
{int min;
    for(int i=0;i<n;i++)
    {
        min=i;
        for(int j=i+1;j<n;j++)
        {
            if(a[j]<a[min])
            {swap(&a[j],&a[i]);
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
   selection_sort(a,n);
   for(int i=0;i<n;i++)
   {
       printf("%d\t",a[i]);
   }

    return 0;
}
