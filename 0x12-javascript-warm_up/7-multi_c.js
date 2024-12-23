#!/usr/bin/node

const num = process.argv[2];
if (num) {
  for (let count = 1; count <= num; count++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occureneces');
}
