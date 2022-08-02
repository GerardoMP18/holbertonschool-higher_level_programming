#!/usr/bin/node
// If w or h is equal to 0 or not a positive integer, create an empty object

module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      return new Rectangle();
    }
    else if (w >= 1 && h >= 1) {
      this.width = w;
      this.height = h;
    }
  }
};
