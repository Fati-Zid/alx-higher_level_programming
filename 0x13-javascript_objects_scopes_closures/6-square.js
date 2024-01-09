#!/usr/bin/node
//  square and inherits from Square
module.exports = class Square extends require('./5-square') {
  // 
  charPrint(c){
    if (c == undefined)
        this.print()
    else
        for (let index = 0; index < this.height; index++) 
            console.log("c".repeat(this.width))
  }
};
