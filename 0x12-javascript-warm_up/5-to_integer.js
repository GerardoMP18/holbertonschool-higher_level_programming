#!/usr/bin/node
// Script that converted to an integer

const myArgv = process.argv[2];

if (isNaN(myArgv)) {
  console.log('Not a number');
} else {
  const convertInteger = Math.floor(myArgv);
  console.log(`My number: ${convertInteger}`);
}
