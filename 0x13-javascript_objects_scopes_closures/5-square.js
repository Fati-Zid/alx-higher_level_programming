#!/usr/bin/node
//  square and inherits from Rectangle
require('./4-rectangle')
class Square extends Rectangle {
    constructor(size) {
        super (size,size);
    }
}