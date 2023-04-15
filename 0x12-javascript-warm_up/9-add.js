#!/usr/bin/node
function add (a, b) {
  const total = a + b;
  console.log(total);
}

const args = process.argv;
const a = parseInt(args[2]);
const b = parseInt(args[3]);
add(a, b);
