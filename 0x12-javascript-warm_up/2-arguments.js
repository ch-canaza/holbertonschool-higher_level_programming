#!/usr/bin/node
const argcounter = process.argv.length;
if (argcounter < 3) {
  console.log('no argument');
} else if (argcounter === 3) {
  console.log('argument found');
} else {
  console.log('arguments found');
}
