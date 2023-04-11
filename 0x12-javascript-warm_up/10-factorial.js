#!/usr/bin/node

const arg = Number(process.argv[2]);

function factorial (num) {
  if (isNaN(num)) {
    return 1;
  }

  if (num === 0) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

const result = factorial(arg);
console.log(result);
