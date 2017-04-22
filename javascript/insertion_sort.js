function insertion_sort(A,n) {
  for (var i=1;i<n;i++){
    var key=A[i];
    var j=i-1;
    while (j>=0 && A[j]>key){
      A[j+1]= A[j]
      j=j-1
     }
    A[j+1]=key
  }
}

var A=[1, 2, 3333,1,4,3,2,888,123123123,123123,123,123];
insertion_sort(A,A.length);
alert(A)
