#!/usr/bin/node
// Print flag depend on argument.

if (process.argv.length < 3) console.log('No argument');
else if (process.argv.length === 3) console.log('Argument found');
else console.log('Arguments found');
