#!/usr/bin/node
// Script that searches the second biggest integer in the list of arguments

const myArgv = process.argv;
const size = myArgv.length;

if (size <= 3) {
  console.log(0);
} else {
  myArgv.sort((a, b) => a - b);
  console.log(myArgv[size - 2]);
}
