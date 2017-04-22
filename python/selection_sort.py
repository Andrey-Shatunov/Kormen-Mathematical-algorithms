def selection_sort(A,n):
  smallest=A[0]
  for i in range(n-1):
    smallest=A[i]
    smallest_index=i
    for j in range(i,n):
      if smallest>A[j]:
        smallest=A[j]
        smallest_index=j 
    tmp=A[i]
    A[i]=A[smallest_index]
    A[smallest_index]=tmp

A=[3,2,1,5,1,2,3,4,1,2,3,5,6,7]
selection_sort(A,len(A))
print(A)