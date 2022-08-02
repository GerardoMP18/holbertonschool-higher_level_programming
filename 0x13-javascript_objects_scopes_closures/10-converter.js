#!/usr/bin/node
// function that converts a number from base10 to another base passed as argument

exports.converter = function (base) {
  function convertBase (number) {
    return (number.toString(base));
  }
  return convertBase;
};
