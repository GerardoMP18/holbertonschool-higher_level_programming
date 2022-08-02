#!/usr/bin/node
// Create an instance method called rotate() that exchanges the width and the height of the rectangle
// Create an instance method called double() that multiples the width and the height of the rectangle by 2

module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      return new Rectangle();
    } else if (w >= 1 && h >= 1) {
      this.width = w;
      this.height = h;
    }
  }

  //creation of method
  print () {
    const character = 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(character.repeat(this.width));
    }
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }

  rotate () {
    const value = this.width;
    this.width = this.height;
    this.height = value;
  }
};
