#!/usr/bin/node
const argument = process.argv[2];
if (isNaN(argument)) {
  console.log('Missing number of occurrences');
} else {
  for (let x = 1; x <= argument; x++) {
    console.log('C is fun');
  }
}
