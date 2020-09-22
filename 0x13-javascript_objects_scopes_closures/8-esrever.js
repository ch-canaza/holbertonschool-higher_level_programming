#!/usr/bin/node
exports.esrever = function (list) {
  const mylist = [];
  for (let i = 0; i < list.length; i++) {
    mylist.unshift(list[i]);
  }
  return mylist;
};
