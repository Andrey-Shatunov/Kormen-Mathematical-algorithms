function binary_search(A, n, x) {
  var p = 0;
  var r = n - 1;
  while (p <= r) {
  	console.log("p",p);
    console.log("r",r);
    var q = (p + r) / 2;
    q = Math.floor(q);
    console.log("q",q);
    if (A[q] == x) {
      return q;
    }
    if (A[q] > x) {
      r = q - 1;
    }
    if (A[q] < x) {
      p = q + 1;
    }
  }
  return "Not found";
}


var a = binary_search([1, 2, 3333], [1, 2, 3].length, 3333);
alert(a)
