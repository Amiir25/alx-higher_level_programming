#!/usr/bin/node

const fs = require('fs');
const file = process.argv[2];

if (!file) {
  console.error('Usage: ./0-readme.js <file_path>');
  process.exit(1);
}

fs.readFile(file, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  }
  console.log(data);
});
