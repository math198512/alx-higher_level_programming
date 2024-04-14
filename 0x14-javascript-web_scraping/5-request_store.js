#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const filepath = process.argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.error(error); // Print the error if one occurred
  } else {
    fs.writeFile(filepath, body, 'utf8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
