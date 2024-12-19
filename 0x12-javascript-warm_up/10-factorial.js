#!/usr/bin/node

const arg = parseInt(process.argv[2]);
let fact = 0;

function factorial (f) {
  fact += f;
  if (f > 0) {
    factorial(f - 1);
  }
}

if (isNaN(arg)) {
  console.log(1);
} else {
  factorial(arg);
  console.log(fact);
}
