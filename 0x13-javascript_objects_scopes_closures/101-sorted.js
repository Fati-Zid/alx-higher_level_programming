#!/usr/bin/node
const oldDict = require('./101-data').dict;
const newDict = {};
for (const val in oldDict) {
  if (oldDict[val] in newDict) {
    newDict[oldDict[val]].push(val);
  } else {
    newDict[oldDict[val]] = [val];
  }
}
console.log(newDict);
