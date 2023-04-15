#!/usr/bin/node
const squareSize = parseInt(process.argv[2]);
const notNumber = isNaN(squareSize);

if (notNumber) {
  console.log('Missing size');
}

for (let count = 0; count < squareSize; count++) {
  console.log('X'.repeat(squareSize));
}
