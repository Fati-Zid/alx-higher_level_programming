#!/usr/bin/node
// script that prints x times “C is fun”
const argv = process.argv[2];
if (isNaN(argv)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i <= parseInt(argv); i++) {
    console.log('C is fun');
  }
}
