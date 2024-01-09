#!/usr/bin/node
// function that returns the reversed version of a list
module.exports.esrever = function (list) {
  // check if input is an array, return error message if not
  if (!Array.isArray(list)) {
    throw new Error('Input should be an array');
  }
  const result = []; // create empty array to store the reversed list in
  for (let i = list.length - 1; i >= 0; i--) {
    result.push(list[i]); // add each element from last to first to the "result" array
  }
  return result;
};
