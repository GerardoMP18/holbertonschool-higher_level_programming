#!/usr/bin/node
// Script that prints a square

const myArgv = process.argv[2];

if (isNaN(myArgv)) {
  console.log('Missing size');
} else {
  const convertInteger = Math.floor(myArgv);

  for (let i = 0; i < convertInteger; i++) {
    console.log('X'.repeat(convertInteger));
  }
}
