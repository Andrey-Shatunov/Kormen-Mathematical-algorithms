#include <stdio.h>


void selection_sort(int *A,int n){
  int smallest=A[0];
  int smallest_index,tmp;
  for(int i=0;i<n;i++){
    smallest=A[i];
    smallest_index=i;
    for(int j=i;j<n;j++){
      if (smallest>A[j]){
        smallest=A[j];
        smallest_index=j;
        printf("%d ",smallest_index);
      }
    }
    tmp=A[i];
    A[i]=A[smallest_index];
    A[smallest_index]=tmp;

  }
  printf("\n");
  for(int i=0;i<n;i++){
      printf("%d ",A[i]);
  }
}

int main()
{
  int A[14]={3,2,1,5,1,2,3,4,1,2,3,5,6,7};
  selection_sort(A,14);
  return 0;
}
