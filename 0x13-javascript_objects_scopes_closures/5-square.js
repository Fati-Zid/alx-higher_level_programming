#!/usr/bin/node
//  square and inherits from Rectangle
module.exports = class Square extends require('./4-rectangle') {
  constructor (size) {
    super(size, size);
  }
};
