#!/usr/bin/node
const argument = process.argv[2];
if (isNaN(argument)) {
  console.log('Missing size');
} else {
  for (let x = 1; x <= argument; x++) {
    let row = '';
    for (let y = 0; y < argument; y++) row += 'X';
    console.log(row);
  }
}
