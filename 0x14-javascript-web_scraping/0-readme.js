#!/usr/bin/node
const fs = require('fs');

var readFile = fs.readFileSync(process.argc[2], 'utf8');
console.log(readFile);
