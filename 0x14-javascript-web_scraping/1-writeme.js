#!/usr/bin/node
const fs = require('fs');
const file = process.argv[2];
const textString = process.argv[3];
fs.writeFile(file, textString, 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
