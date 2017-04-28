def compute_lcs_table(X,Y):
  m = len(X)+1
  n = len(Y)+1
  l = [[0] * n for i in range(m)]
  for i in range(0,m-1):
    for j in range(0,n-1):
      if X[i]==Y[j]:
        print(X[i]+"<=X Y=>"+str(Y[j]))
        l[i+1][j+1]=l[i][j]+1
      else:
        l[i+1][j+1]=max(l[i+1][j], l[i][j+1])
 
  for i in range(0,m):
    print(l[i])
  
  

compute_lcs_table("catcga","ctaccgtca")
