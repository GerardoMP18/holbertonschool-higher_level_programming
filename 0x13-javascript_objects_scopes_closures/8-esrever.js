#!/usr/bin/node
// Function that returns the reverse version of a list

exports.esrever = function (list) {
  const newArray = [];
  const size = list.length - 1;

  for (let i = size; i >= 0; i--) {
    newArray.push(list[i]);
  }
  return newArray;
};
