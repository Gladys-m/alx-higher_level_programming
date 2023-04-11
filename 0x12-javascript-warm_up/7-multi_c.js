#!/usr/bin/node

const arg = process.argv[2];
const num = Number(arg);
const line = 'C is fun';

if (!num) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < num; i++) {
    console.log(line);
}
