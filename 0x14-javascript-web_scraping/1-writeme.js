#!/usr/bin/node

const fs = require('fs');
const file = process.argv[2];
const content = process.argv.slice(3).join(' ');

if (!file || !content.trim()) {
  console.error('Usage: ./1-writeme.js <file_path> <String>');
  process.exit(1);
}

fs.writeFile(file, content, 'utf8', (err) => {
  if (err) {
    console.log(err);
  }
});
