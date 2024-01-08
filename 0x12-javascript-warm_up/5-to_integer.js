#!/usr/bin/node
// is an integer

if (typeof (parseInt(process.argv[2]) != Number)) console.log('Not a number');
else console.log('My number: ', process.argv[2]);
