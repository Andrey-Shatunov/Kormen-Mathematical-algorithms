def fl_w(graph,n):
  
  shortest = [[graph[i][j] for j in range(n)] for i in range(n)] 
  for k in range(n): 
      for i in range(n):
          for j in range(n): 
              shortest[i][j] = min(shortest[i][j], shortest[i][k] + shortest[k][j])
              
  print(shortest)

graph=[[100000000,6,4,100000000,100000000],
       [100000000,100000000,2,3,100000000],
       [100000000,1,100000000,7,3],
       [100000000,100000000,100000000,100000000,4],
       [7,100000000,100000000,5,100000000]]
       
fl_w(graph,5)
