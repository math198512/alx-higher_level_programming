#!/usr/bin/node

const { argv } = require('node:process');

let message = 'No argument';

if (argv.length === 2) {
  message = 'No argument';
} else if (argv.length === 3) {
  message = 'Argument found';
} else {
  message = 'Arguments found';
}

console.log(message);
