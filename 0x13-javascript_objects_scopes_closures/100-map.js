#!/usr/bin/node
const list = require('./100-data').list;
const myList = list.map((value, index) => {
  return (value * index);
});
console.log(list);
console.log(myList);
