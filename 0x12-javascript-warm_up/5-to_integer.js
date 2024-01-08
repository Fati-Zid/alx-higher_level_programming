#!/usr/bin/node
// is an integer

if (process.argv[2] === undefined || typeof parseInt(process.argv[2]) != Number)
  console.log('Not a number');
else console.log('My number: ', process.argv[2]);
