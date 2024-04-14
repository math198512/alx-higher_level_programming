#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error); // Print the error if one occurred
  } else {
    const obj = JSON.parse(body);
    const movies = obj.results;
    const moviesNumber = movies.length;
    let counter = 0;
    const regex1 = /people\/18\/$/;
    for (let i = 0; i < moviesNumber; i++) {
      const characters = movies[i].characters;
      const charactsNum = characters.length;
      for (let j = 0; j < charactsNum; j++) {
        const str1 = characters[j];
        if (regex1.exec(str1) !== null) {
          counter++;
        }
      }
    }
    console.log(counter);
  }
});
