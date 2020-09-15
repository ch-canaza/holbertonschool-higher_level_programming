#!/usr/bin/node
const argcounter = process.argv.length;
if (argcounter < 3) {
  console.log('No argument');
} else if (argcounter === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
