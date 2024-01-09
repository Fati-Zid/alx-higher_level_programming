#!/usr/bin/node
// function that prints the number of arguments already printed and the new argument value.
logsCount = 0;
module.exports.logMe = function (item) {
  console.log(this.logsCount + ': ' + this.item);
  logsCount++;
};
