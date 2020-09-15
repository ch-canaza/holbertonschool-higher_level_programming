#!/usr/bin/node
const argcounter = process.argv[2];
if (argcounter === undefined) {
  console.log('No argument');
} else {
  console.log(argcounter);
}
