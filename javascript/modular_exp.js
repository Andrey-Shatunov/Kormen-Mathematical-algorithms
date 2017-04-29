
// x^d mod n
function modular_exp(x,d,n) {
  if(d==0){
  	return 1;
  }
  else if((d%2)==0){
  	var z=modular_exp(x,d/2,n);
    return ((z*z)%n);
  }
  else if((d%2)==1){
    var z=modular_exp(x,(d-1)/2,n);
    return (z*z*x)%n;
  }
}

z=modular_exp(2,3,3);
alert(z);
