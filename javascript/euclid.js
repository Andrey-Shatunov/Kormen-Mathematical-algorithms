function euclid(a, b) {
  
  if(b == 0)
  	return [a, 1, 0];
  else{
  	var mass=euclid(b, a%b);
    var i = mass[2];
    var j = mass[1] - (a / b * mass[2]);
    return [mass[0], i , j];
  }
}

mass=euclid(12, 16);
alert( mass[0] );
