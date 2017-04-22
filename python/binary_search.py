def binary_search(A,n,x):
  p=0
  r=n-1
  while p<=r:
    #print("r= "+str(r)+" p= "+str(p))
    q=(p+r)//2
    #print("q= "+str(q))
    if A[q]==x:
      return q
    elif A[q]>x:
      r=q-1
    elif A[q]<x:
      p=q+1
    
  return "Not found"
  
  
A=[0,1,2,3,4,5,6,7,8,9]
a=binary_search(A,len(A),9)
print(a)