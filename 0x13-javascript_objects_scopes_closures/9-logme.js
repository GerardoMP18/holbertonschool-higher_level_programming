#!/usr/bin/node
// Function that prints the number of arguments already printed and the new arguments value

let contador = 0;
exports.logMe = function (item) {
  console.log(contador + ': ' + item);
  contador += 1;
};
