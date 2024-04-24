#!/usr/bin/node
const args = process.argv.slice(2);

if (args.length === 0 || args.length === 1) {
  console.log('0');
} else {
  // Convert the argument to numbers
  const numbers = args.map(array => parseInt(array, 10));

  // Find the largest number from the array
  const largest = Math.max(...numbers);

  // Remove largest number from the array
  args.splice(numbers.indexOf(largest), 1);

  // Find the second largest number
  const secondLargest = Math.max(...args);

  // Print the second largest number
  console.log(secondLargest);
}
