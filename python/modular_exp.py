# x^d mod n
def modular_exp(x,d,n):
  if d==0:
    return 1
  elif (d%2)==0:
    tmp=d/2
    z=modular_exp(x,tmp,n)
    return ((z*z)%n)
  elif (d%2)==1:
    tmp=(d-1)/2
    z=modular_exp(x,tmp,n)
    return (z*z*x)%n

z=modular_exp(5,6,3)
print(z)
