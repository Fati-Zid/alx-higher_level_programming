#!/usr/bin/node
// Factorial numbers
const args = process.argv.slice(2);
const a = parseInt(args[0]);
console.log(factorial(a));

function factorial(a) {
  if (a > 1) {
    return a * factorial(a - 1);
  } else {
    return 1;
  }
}
