#!/usr/bin/node
const args = process.argv.slice(2);
const numArg = parseInt(args[0], 10);

if (args.length === 0 || isNaN(numArg)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${numArg}`);
}
