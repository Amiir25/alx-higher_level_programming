#!/usr/bin/node
const len = process.argv;
if (len.length <= 2) {
  console.log('No Argument');
} else if (len.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
