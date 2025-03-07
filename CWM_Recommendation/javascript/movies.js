const K = 3;

module.exports.listSimilarity=listSimilarity;
function listSimilarity(list1,list2) {
 return list1.intersection(list2).size/list1.union(list2).size;
}

module.exports.personSimilarity=personSimilarity;
function personSimilarity(p1,p2) {
 var cat = listSimilarity(p1.categories,p2.categories);
 var mov = listSimilarity(p1.movies,p2.movies);
 return cat+mov;
}

module.exports.loadUsers=loadUsers;
function loadUsers() {
 var json = require('./movies.json');
 json.forEach(i=>i.movies = new Set(i.movies));
 json.forEach(i=>i.categories = new Set(i.categories));
 return json;
}

module.exports.run=run;
function run() {
 var users = loadUsers();
 console.log('users length',users.length);
 for(var query of users) {
  var distances = users.map(i=>personSimilarity(i,query));
  var sortIndexes = Object.keys(distances).sort((a,b)=>distances[b]-distances[a])
  var topIndexes = sortIndexes.slice(1,K+1);  //Assuming top match is self
  var sortedTargets = sortIndexes.map(idx=>users[idx]);
  //if(sortedTargets[0]==query) console.log('Good, first is self',query.name);
  //console.log(query.name,sortedTargets[0].name);
  var topK = sortedTargets; //We reduced the list at the indexes
  var peerMovies = topK.reduce((acc,peer)=>acc.concat(Array.from(peer.movies)),[]);
  var moviesFiltered = peerMovies.filter(i=>!query.movies.has(i));
  var counts=require('lodash').countBy(moviesFiltered);
  var tupleCount = Object.keys(counts).map(i=>[i,counts[i]]);
  tupleCount.sort((a,b)=>b[1]-a[1]);
  //console.log(tupleCount);
  console.log(query.name+':')
  var movieList = tupleCount.slice(0,3).map(i=>i[0]);
  for(var movie of movieList) {
   console.log('    '+movie);
  }
  
 }
}
