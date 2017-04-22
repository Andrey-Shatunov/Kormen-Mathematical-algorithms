def recurcive_binary_search(A,p,r,x):
  if p>r:
    return "Not found"
  elif p<=r:
    q=(p+r)//2
    if A[q]==x:
      return q
    elif A[q]>x:
      return recurcive_binary_search(A,p,q-1,x)
    elif A[q]<x:
      return recurcive_binary_search(A,q+1,r,x)
  
  
A=[3,5,7]
a=recurcive_binary_search(A,0,(len(A)-1),78)
print(a)