def sentinal_linear_search(A,n,x):
  last=A[len(A)-1]
  A[len(A)-1]=x
  for i in range(n):
    I=i
    if A[i]==x:
      break
    
  A[len(A)-1]=last
  if I<n-1 or A[n-1]==x:
    #print("I="+str(I))
    return I
  else:
    return "not found"
    
A=[1,2,3,4,5]
print(sentinal_linear_search(A,len(A),4))