#!/usr/bin/node
const args = process.argv.slice(2);

function factorial (num) {
  if (num === 0) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

if (args.length === 0) {
  console.log('1');
} else {
  const number = parseInt(args[0], 10);
  if (isNaN(number)) {
    console.log('1');
  } else {
    const func = factorial(number);
    console.log(func);
  }
}
