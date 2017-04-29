#include <stdio.h>

void main()
{
  int n=5;
  int graph[5][5]={{0,6,4,0,0},
       {0,0,2,3,0},
       {0,1,0,7,3},
       {0,0,0,0,4},
       {7,0,0,5,0}};
  
  int shortest[5]={0,100000000,100000000,100000000,100000000};
  int pred[5]={0,0,0,0,0};
  
  for(int k=0;k<n-1;k++)
  {
    for(int u=0;u<n;u++)
    {
       for(int v=0;v<n;v++)
      {
        if (graph[u][v]!=0)
        {
          if ((shortest[u]+graph[u][v])<shortest[v])
          {
            shortest[v]=shortest[u]+graph[u][v];
            pred[v]=u;
          }
        }
      }
    }
  }
  for(int u=0;u<n;u++)
    {
        printf("%d ",shortest[u]);
    }
  return 0;
}
