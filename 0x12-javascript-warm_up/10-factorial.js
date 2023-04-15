#!/usr/bin/node
function factorial (number) {
  const notNum = isNaN(number);
  if (notNum || number === 0) {
    return (1);
  }
  return (number * factorial(number - 1));
}

const args = process.argv;
const num = parseInt(args[2]);
console.log(factorial(num));
