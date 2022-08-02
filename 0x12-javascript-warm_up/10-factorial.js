#!/usr/bin/node
// Script that computes and prints a factorial

function factorial (n) {
  if (isNaN(n) || n <= 0) {
    return (1);
  } else {
    return (parseInt(n) * factorial(n - 1));
  }
}

const myArgv = process.argv[2];

console.log(factorial(parseInt(myArgv)));
