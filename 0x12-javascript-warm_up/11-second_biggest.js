#!/usr/bin/node

const args = process.argv.slice(2);
const len = args.length;

if (len < 2) {
  console.log(0);
} else {
  let largest = -Infinity;
  let secondLargest = -Infinity;
  for (let i = 0; i < len; i++) {
    const current = parseInt(args[i]);
    if (current > largest) {
      secondLargest = largest;
      largest = current;
    } else if (current > secondLargest) {
      secondLargest = current;
    }
  }

  console.log(secondLargest);
}
