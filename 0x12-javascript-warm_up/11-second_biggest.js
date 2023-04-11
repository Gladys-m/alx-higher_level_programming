#!/usr/bin/node

const args = process.argv.slice(2).map(Number);
const len = args.length;

if (len < 2) {
  console.log(0);
} else {
  const sortedArgs = args.sort((a, b) => a - b);
  const secondSmallest = sortedArgs[1];
  console.log(secondSmallest);
}
