#!/usr/bin/node
// Arguments handling
const args = process.argv;
console.log(args[2]);
if (typeof args[2] === 'undefined') {
  console.log('No argument');
} else {
  console.log(args[2]);
}
