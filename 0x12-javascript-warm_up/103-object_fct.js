#!/usr/bin/node
// Script by adding a new function that increments the integer
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
myObject.incr = () => {
  return myObject.value++;
};
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
