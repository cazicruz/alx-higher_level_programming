#!/usr/bin/node
const fs = require('fs');
fs.writeFile(process.argv[1],process.argv[3], function (error) {
  if (error){
    console.log(error);}
});
