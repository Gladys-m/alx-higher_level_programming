#!/usr/bin/node

const arg1 = process.argv[2];
const arg2 = process.argv[3];

function add(a, b) {
  return a * b;
}

const result = add(arg1, arg2);
console.log(result);
