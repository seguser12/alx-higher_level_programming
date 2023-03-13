#!/usr/bin/node
const args = process.argv;
if (args.length <= 3) {
  console.log('0');
} else {
  const arr = args.slice(2).map(Number);
  const max = Math.max.apply(null, arr);
  arr.splice(arr.indexOf(max), 1);
  const secondMax = Math.max.apply(null, arr);
  console.log(secondMax);
}
