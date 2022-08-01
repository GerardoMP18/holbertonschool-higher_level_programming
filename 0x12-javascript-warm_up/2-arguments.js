#!/usr/bin/node
// Script that print a message depending of the number of arguments passed

const myArgv = process.argv.length;

if (myArgv === 2) {
  console.log('No argument');
}
else if (myArgv === 3) {
  console.log('Argument found');
}
else {
  console.log('Arguments found');
}
