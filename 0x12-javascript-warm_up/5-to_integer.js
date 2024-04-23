#!/usr/bin/node
const args = process.argv.slice(2);

if (args.length === 0) {
  console.log('Not a number');
} else {
  const numArg = parseInt(args[0], 10);
  console.log(numArg);
}
