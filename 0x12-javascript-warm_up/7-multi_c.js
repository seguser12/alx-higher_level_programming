#!/usr/bin/node
let count = parseInt(process.argv[2]);

if (isNaN(count)) {
  console.log('Missing number of occurences');
}

while (count > 0) {
  console.log('c is fun');
  count -= 1;
}
