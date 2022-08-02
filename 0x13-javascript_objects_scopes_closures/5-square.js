#!/usr/bin/node
// Creation of class square with inherits from rectangle

const Rectangle = require('./4-rectangle.js');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
