#!/usr/bin/node
// Script that print x times  C is fun

const myArgv = process.argv[2];

if (isNaN(myArgv)) {
  console.log('Missing number of occurrences');
} else {
  const convertInteger = Math.floor(myArgv);

  for (let x = 0; x < convertInteger; x++) {
    console.log('C is fun');
  }
}
