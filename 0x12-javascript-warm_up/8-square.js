#!/usr/bin/node

const num = parseInt(process.argv[2]);

if (!isNaN(num)) {
  for (let i = 1; i <= num; i++) {
    let x = '';
    for (let j = 1; j <= num; j++) {
      x += 'X';
    }
    console.log(x);
  }
} else {
  console.log('Missing size');
}
