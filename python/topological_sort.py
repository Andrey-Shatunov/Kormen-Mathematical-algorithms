def topological_sort(graph,n):
  in_degree=[]
  next=[]
  line_up=[]
  
  for i in range(n):
    in_degree.append(0)
    
  for i in range(len(graph)):
    in_degree[graph[i][1]]+=1
  
  for i in range(n):
    if in_degree[i]==0:
      next.append(i)
    
  while len(next)!=0:
    u=next.pop()
    line_up.append(u)
    for i in range(len(graph)):
      if in_degree[graph[i][0]]==u:
        in_degree[graph[i][1]]-=1
        if in_degree[graph[i][1]]==0:
          line_up.append(graph[i][1])
  
  return line_up
        
        
graph=[[0,1],[0,2],[1,3],[2,3]]
line_up=topological_sort(graph,4)
print(line_up)
