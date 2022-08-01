#!/usr/bin/node
// Script that print x times  C is fun

const myArgv = process.argv[2];

if (isNaN(myArgv)) {
  console.log('Missing number of occurrences');
} else {
  const convertInteger = Math.floor(myArgv);
  
  for (let i = 0; i < convertInteger; i++) {
    console.log('C is fun');
  }
}
