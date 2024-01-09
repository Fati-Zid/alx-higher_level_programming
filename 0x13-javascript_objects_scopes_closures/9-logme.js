#!/usr/bin/node
// function that prints the number of arguments already printed and the new argument value.
let logsCount = 0;
module.exports.logMe = function (item) {
  console.log(logsCount + ': ' + item);
  logsCount++;
};
