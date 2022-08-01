#!/usr/bin/node
// Script that prints the addition of 2 integers

function add (a, b) {
 return (a + b);
}

const myArgv = process.argv;

console.log(add(parseInt(myArgv[2]), parseInt(myArgv[3])));
