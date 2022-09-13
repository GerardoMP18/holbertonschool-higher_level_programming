#!/usr/bin/node
// script that writes a string to a file

const fs = require('fs');
const filePath = process.argv[2];
const textWrite = process.argv[3];

fs.writeFile(filePath, textWrite, 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
