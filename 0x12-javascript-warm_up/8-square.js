#!/usr/bin/node
const args = process.argv.splice(2);
const numConvert = parseInt(args[0], 10);

if (args.length === 0 || isNaN(numConvert)) {
  console.log('Missing size');
}

for (let i = 0; i < numConvert; i++) {
  for (let j = 0; j < numConvert; j++) {
    process.stdout.write('X');
  }

  console.log('\n');
}
