//Write a program to sort an array using merge sort

//quick sort

// implement stack using array

#include <stdio.h>

int main(){
    int a[10],b[10],merged[20];
    int n1,n2,i,j,k;

    printf("Enter number of elements in First Sorted Array:");
    scanf("%d",&n1);

    printf("Enter %d elements in First Sorted Array:",n1);
    for (i=0;i<n1;i++){
            scanf("%d",&a[i]);
    }
    printf("Enter number of elements in Second Sorted Array:");
    scanf("%d",&n2);

    printf("Enter %d elements in Second Sorted Array:",n2);
    for (i=0;i<n2;i++){
            scanf("%d",&b[j]);
    }

     for (i=0;i<n1; i++) {
        merged[i] = a[i];
    }
    for (j=0;j<n2;j++) {
        merged[i+j]=b[j];
    }

    int n=n1+n2;

    for (i=0;i<n-1;i++) {
        for (j=0;j<n-1-i;j++) {
            if (merged[j]>merged[j+1]) {
                int temp=merged[j];
                merged[j]=merged[j+1];
                merged[j+1]=temp;
            }
        }
    }
    printf("Merged and sorted Array:\n");
    for(i=0;i<n;i++){
        printf("%d\n",merged[i]);
    }
    return 0;
}
