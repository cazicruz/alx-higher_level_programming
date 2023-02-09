#!/usr/bin/node
// a script that reads to stdout


const fs = require('fs');
var readFile = fs.readFileSync(process.argc[2], 'utf8');
console.log(readFile);
