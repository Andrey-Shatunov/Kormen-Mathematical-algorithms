def euclid(a,b):
  if b==0:
    return (a,1,0)
  else:
    g,i1,j1=euclid(b,a%b)
    i=j1
    j=i1-(a//b*j1)
    return (g,i,j)
  
def asd(a,b):
  return (1,2,3)
  
  
g,i,j=euclid(9,6)
print(g)
