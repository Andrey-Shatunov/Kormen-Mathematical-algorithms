def partition(A,p,r):
  q=p 
  for u in range(p,r):
    if A[u]<=A[r]:
      tmp=A[u]
      A[u]=A[q]
      A[q]=tmp
      q=q+1
      
  tmp=A[q]
  A[q]=A[r]
  A[r]=tmp
  return q
  
def quick_sort(A,p,r):
  if p<r:
    q=partition(A,p,r)
    quick_sort(A,p,q-1)
    quick_sort(A,q,r)


A=[111,3,2,1,4,5,2,1]
quick_sort(A,0,len(A)-1)
print(A)
