#!/usr/bin/node
const args = process.argv.slice(2);

function add (a, b) {
  const num1 = parseInt(a, 10);
  const num2 = parseInt(b, 10);

  console.log(num1 + num2);
}

add(args[0], args[1]);
