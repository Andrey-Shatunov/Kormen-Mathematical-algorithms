function sentinal_linear_search(A,n,x) {
	var last=A[A.length-1];
  var I;
  A[A.length-1]=x;
  for(i=0;i<A.length;i++)
  {
  	I=i;
    if(A[i]==x)
    	break;
  }
  A[A.length-1]=last;
  if (I<n-1 || A[n-1]==x)
  {
    return I;
  }
  else{
    return "not found";
  }
}


var a = sentinal_linear_search([1,2,3],[1,2,3].length,2);
alert(a)