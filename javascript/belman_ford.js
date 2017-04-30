function belman_ford(graph, s) {
  var n = graph.length;
  var shortest = [];
  var pred = [];
//  
  for(var i = 0; i < n; i++){
  	shortest.push(1000000);
    pred.push("None")
  }
//
  shortest[0] = 0;
//
  for(var i = 0 ; i < n-1; i++){
  	for(var u = 0;u < n; u++){
    	for(var v = 0; v < n; v++){
      	if (graph[u][v] != 0){
        	if ((shortest[u] + graph[u][v]) < shortest[v]){
            shortest[v] = shortest[u]+graph[u][v];
            pred[v] = u;
           }
        }
      }
    }
  }
//  
  alert( shortest );
  alert( pred );
}
var graph = [[0,6,4,0,0],
       [0,0,2,3,0],
       [0,1,0,7,3],
       [0,0,0,0,4],
       [7,0,0,5,0]]; 

belman_ford(graph, 0)
