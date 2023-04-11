#!/usr/bin/node

const arg = process.argv[2];
const num = Number(arg);

if (!num) {
  console.log('Missing size');
}

for (let i = 0; i < num; i++) {
  let row = '';
  for (let j = 0; j < num; j++) {
    row += 'x';
  }
  console.log(row);
}
