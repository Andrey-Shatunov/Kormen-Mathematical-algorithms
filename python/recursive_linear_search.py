def recursive_linear_search(A,n,i,x):
  if i>=n:
    return "NOT FOUND"
  elif A[i]==x:
    return i
  else:
    return recursive_linear_search(A,n,i+1,x)
    
A=[1,2,3,4,5]
print(recursive_linear_search(A,len(A),0,6))