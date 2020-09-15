#!/usr/bin/node
const argument = process.argv[2];
if (isNaN(argument)) {
  console.log('Not a number');
} else {
  console.log('my number: ' + argument);
}
