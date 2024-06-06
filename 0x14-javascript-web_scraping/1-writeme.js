#!/usr/bin/node
/* A script that writes a string to a file. */

const fs = require('fs');
const filename = process.argv[2];
const data = process.argv[3];

fs.writeFile(filename, data, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});
