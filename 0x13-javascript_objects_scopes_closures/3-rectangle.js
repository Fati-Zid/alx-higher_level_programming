#!/usr/bin/node
// class Rectangle that defines a rectangle with constructor and check if argument was empty
module.exports = class Rectangle {
  // constructor  take 2 arguments w and h
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  // method print()
  print () {
    for (let i = 0; i<this.height; i++) {
        console.log('X'.repeat(this.width));
    }
  }
};
