function recursive_linear_search(A,n,i,x) {
	if(i>=n){
  	return "NOT FOUND"
  }
  else{
  	if(A[i]==x){
    	return i;
    }
    else{
    	return recursive_linear_search(A,n,i+1,x);
    }
  }
}


var a = recursive_linear_search([1,2,3],[1,2,3].length,0,5);
alert(a)