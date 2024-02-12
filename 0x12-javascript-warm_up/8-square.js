#!/usr/bin/node
// three languages
const Hor = [];
const args = process.argv.slice(2);
if (args.length < 1) {
  console.log('Missing size');
} else if (isNaN(parseInt(args[0]))) {
  console.log('Missing size');
} else {
  const x = args[0];
  for (let i = x; i > 0; i--) {
    Hor.push('X');
  }
  for (let i = x; i > 0; i--) {
    console.log(Hor.join(''));
  }
}
