#!/usr/bin/node

function factorial (f) {
  if (isNaN(f)) {
    return 1;
  }
  if (f <= 1) {
    return 1;
  }

  return f * factorial(f - 1);
}

const fact = parseInt(process.argv[2], 10);
console.log(factorial(fact));
