#include <stdio.h>


int sentinal_linear_search(int *A,int n,int x){
  int last=A[n-1];
  int I;
  A[n-1]=x;
  for(int i=0;i<n;i++){
    I=i;
    if (A[i]==x)
      break;
  }
    
  A[n-1]=last;
  if ((I<n-1) || (A[n-1]==x))
    return I;
  else{
    return "10000000000000";}
}

int main()
{
  int A[4]={3,2,1,5};
  int y=sentinal_linear_search(A,4,5);
  printf("%d",y);
  return 0;
}
