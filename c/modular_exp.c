// x^d mod n
#include <stdio.h>

int modular_exp(int x,int d,int n){
  if(d==0){
  	return 1;
  }
  if((d%2)==0){
  	int z=modular_exp(x,d/2,n);
    return ((z*z)%n);
  }
  if((d%2)==1){
    int z=modular_exp(x,(d-1)/2,n);
    return (z*z*x)%n;
  }
}

void main()
{
  int z=modular_exp(5,6,3);
  printf("%d",z);
  return 0;
}
