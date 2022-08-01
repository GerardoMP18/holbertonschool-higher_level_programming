#!/usr/bin/node
// Script that prints the fist arguments passed to it

const myArgv = process.argv[2];

if (myArgv === undefined) {
  console.log('No argument');
} else {
  console.log(myArgv);
}
