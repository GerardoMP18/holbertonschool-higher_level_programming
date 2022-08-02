#!/usr/bin/node
// Function that increments and calls a function

exports.addMeMaybe = function (number, theFunction) {
  return theFunction(number = number + 1);
}
