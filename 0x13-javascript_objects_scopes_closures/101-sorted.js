#!/usr/bin/node
const dictionary = require('./101-data').dict;

const valueDict = Object.values(dictionary);
const keyDict = Object.keys(dictionary);
const newDict = {};

valueDict.forEach(elements => {
  newDict[elements] = keyDict.filter(key => dictionary[key] === elements);
});
console.log(newDict);
