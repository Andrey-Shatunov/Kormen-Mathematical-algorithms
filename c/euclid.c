#include <stdio.h>

int * euclid(int a,int b){
  if(b==0){
  	int c[3]={a,1,0};
  	int *p=c;
    return p;
  }
  else{
  	int * mass=euclid(b,a%b);
    int i=mass[2];
    int j=mass[1]-(a/b*mass[2]);
    int c[3]={mass[0],i,j};
    int *p=c;
    return p;
  }
  
}

void main()
{
  int * mass=euclid(12, 16);
  printf("%d",mass[0]);
  return 0;
}
