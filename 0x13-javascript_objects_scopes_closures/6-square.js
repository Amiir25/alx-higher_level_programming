#!/usr/bin/node
const parentSquare = require('./5-square');

class Square extends parentSquare {
  constructor (square) {
    super(square, square);
  }

  charPrint (c) {
    const exec = c || 'X';
    for (let i = 0; i < this.height; i++) {
      let temp = '';
      for (let j = 0; j < this.height; j++) {
        temp += exec;
      }
      console.log(temp);
    }
  }
}

module.exports = Square;
