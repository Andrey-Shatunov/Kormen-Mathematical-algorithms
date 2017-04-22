function selection_sort(A,n) {
	var smallest=A[0]
  for (var i=0;i<n-1;i++){
    var smallest=A[i];
    var smallest_index=i;
    for (var j=i;j<n;j++){
      if (smallest>A[j])
      {
        smallest=A[j];
        smallest_index=j ;
      }
    }
    var tmp=A[i];
    A[i]=A[smallest_index];
    A[smallest_index]=tmp;
   }
}

var A=[1, 2, 3333,1,4,3,2,888,123123123,123123,123,123];
selection_sort(A,A.length);
alert(A)
