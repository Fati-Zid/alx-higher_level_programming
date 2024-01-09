#!/usr/bin/node
// function that prints the number of arguments already printed and the new argument value.
module.exports.logMe = function (item) {
    console.log(this.logsCount + ": "+ this.item);
    this.logsCount++;
}