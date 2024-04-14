#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error); // Print the error if one occurred
  } else {
    const obj = JSON.parse(body);
    const moviesNumber = obj.results.length;
    let counter = 0;
    for (let i = 0; i < moviesNumber; i++) {
      if (obj.results[i].characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
        counter++;
      }
    }
    console.log(counter);
  }
});
