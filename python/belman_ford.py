def belman_ford(graph,s):
  n=len(graph)
  shortest = [1000000]*n
  shortest[s]=0 
  pred=[None]*n
  Q=[i for i in range(0,n)]
  
  #while len(Q)!=0:
  for qwe in range(n-1):
    for u in range(n):
      #u=Q.pop(Q.index(min_Q(Q,shortest)))
      for v in range(n):
        if graph[u][v]!=0:
          if (shortest[u]+graph[u][v])<shortest[v]:
            shortest[v]=shortest[u]+graph[u][v]
            pred[v]=u
  print(shortest)
  print(pred)
      
graph=[[0,6,4,0,0],
       [0,0,2,3,0],
       [0,1,0,7,3],
       [0,0,0,0,4],
       [7,0,0,5,0]]
       
belman_ford(graph,0)
