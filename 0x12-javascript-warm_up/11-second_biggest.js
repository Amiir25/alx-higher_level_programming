#!/usr/bin/node

const arr = process.argv.slice(2).map(arg => parseInt(arg, 10));

if (arr.length < 2) {
  console.log(0);
} else {
  const newArr = [...new Set(arr)].sort((a, b) => b - a);
  console.log(newArr[1] || 0);
}
