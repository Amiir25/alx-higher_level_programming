#!/usr/bin/node
const parentSquare = require('./5-square');

class Square extends parentSquare {
  constructor (square) {
    super();
    this.square = square;
  }

  charPrint (c) {
    const exec = c ? 'C' : 'X';
    for (let i = 0; i < this.square; i++) {
      let temp = '';
      for (let j = 0; j < this.square; j++) {
        temp += exec;
      }
      console.log(temp);
    }
  }
}

module.exports = Square;
