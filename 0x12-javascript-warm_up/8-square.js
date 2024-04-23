#!/usr/bin/node
const args = process.argv.splice(2);
const numConvert = parseInt(args[0], 10);

if (args.length === 0 || isNaN(numConvert)) {
  console.log('Missing size');
}

for (let i = 0; i < numConvert; i++) {
  console.log('X'.repeat(numConvert));
}
