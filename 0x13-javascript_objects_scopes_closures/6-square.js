#!/usr/bin/node
// Creation of new methods charPrint that prints the recatngles using the character c o x

const newSquare = require('./5-square');

module.exports = class Square extends newSquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.width; i++) {
        console.log(c.repeat(this.height));
      }
    }
  }
};
