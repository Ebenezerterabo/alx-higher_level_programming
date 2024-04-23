#!/usr/bin/node
const args = process.argv.slice(2);
const numArg = parseInt(args[0], 10);

if (args.length === 0) {
  console.log('Missing number of occurrences');
}

for (let i = 0; i < numArg; i++) {
  console.log('C is fun');
}
