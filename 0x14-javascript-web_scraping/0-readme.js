#!/usr/bin/node
// script that reads and prints the content of a file

const fs = require('fs');
const myArgv = process.argv[2];

fs.readFile(myArgv, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
