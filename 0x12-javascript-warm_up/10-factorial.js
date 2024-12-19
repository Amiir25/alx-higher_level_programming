#!/usr/bin/node

const arg = parseInt(process.argv[2]);
let fact = 0;

for (let i = arg; i > 0; i--) {
  fact += i;
}

if (isNaN(arg)) {
  console.log(1);
} else {
  console.log(fact);
}
