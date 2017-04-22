def merge(A,p,q,r):
  n1=q-p+1
  n2=r-q
  print("A="+str(A))
  print("p="+str(p))
  print("r="+str(r))
  print("q="+str(q))

  B=A[p:q+1]
  C=A[q+1:r+1]
  B.append(10000000)
  C.append(10000000)
  print("B="+str(B))
  print("C="+str(C))

  i,j=0,0
  for k in range(p,r+1):
    if B[i]<=C[j]:
      A[k]=B[i]
      i=i+1 
    elif B[i]>C[j]:
      A[k]=C[j]
      j=j+1 
  print("Aend="+str(A))
  
def merge_sort(A,p,r):
  if p>=r:
    return
  else:
    q=(p+r)//2
    merge_sort(A,p,q)
    merge_sort(A,q+1,r)
    merge(A,p,q,r)
  
  
  
  

A=[5,4,5,6]
merge_sort(A,0,len(A)-1)
print(A)