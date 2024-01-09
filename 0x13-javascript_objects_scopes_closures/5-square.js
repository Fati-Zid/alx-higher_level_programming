#!/usr/bin/node
//  square and inherits from Rectangle
modules.export = class Square extends  require('./4-rectangle') {
    constructor(size) {
        super (size,size);
    }
}
