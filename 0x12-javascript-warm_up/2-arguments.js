#!/usr/bin/node
const args = process.argv.slice(2);
const numArgs = args.length;

if (numArgs === 0) {
  console.log('No Arguments');
} else {
  console.log('Arguments found');
}
