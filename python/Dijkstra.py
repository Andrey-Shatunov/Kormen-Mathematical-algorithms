def min_Q(Q,shortest):
  tmp=1000000000
  for i in Q:
    if shortest[i]<tmp:
      tmp=shortest[i]
      tmp_i=i
  return tmp_i
  
def Dijkstra(graph,s):
  n=len(graph)
  shortest = [1000000]*n
  shortest[s]=0 
  pred=[None]*n
  Q=[i for i in range(0,n)]
  
  while len(Q)!=0:
    u=min_Q(Q,shortest)
    Q.pop(Q.index(u))
    
    for v in range(n):
      if graph[u][v]!=0:
        if (shortest[u]+graph[u][v])<shortest[v]:
          shortest[v]=shortest[u]+graph[u][v]
          pred[v]=u
    
  print(shortest)
      
graph=[[0,6,4,0,0],
       [0,0,2,3,0],
       [0,1,0,7,3],
       [0,0,0,0,4],
       [7,0,0,5,0]]
       
Dijkstra(graph,0)
