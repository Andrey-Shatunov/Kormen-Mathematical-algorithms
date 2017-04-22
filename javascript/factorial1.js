function factorial1(x) {
	if(x==0)
  	return 1;
   else
   	return x*factorial1(x-1)
}

alert(factorial1(3))