#!/usr/bin/node
// Is it a number
const args = process.argv.slice(2);
if (args.length < 1) {
  console.log('Not a number');
} else if (isNaN(parseInt(args[0]))) {
  console.log('Not a number');
} else {
  console.log('My number: '.concat(parseInt(args[0])));
}
