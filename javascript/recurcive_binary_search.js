function recurcive_binary_search(A,p,r,x) {
	if (p>r)
    return "Not found";
  if (p<=r){
   var q=(p+r)/2
   q=Math.floor(q)
    if (A[q]==x)
      return q;
    if (A[q]>x)
      return recurcive_binary_search(A,p,q-1,x);
    if (A[q]<x)
      return recurcive_binary_search(A,q+1,r,x);
  }
}


var a = recurcive_binary_search([1, 2, 3333],0, [1, 2, 3].length-1, 3333);
alert(a)