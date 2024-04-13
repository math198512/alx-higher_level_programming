#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request(url, function (error, response, body) {
  if (error) {
    console.error(error); // Print the error if one occurred
  } else {
    const obj = JSON.parse(body);
    console.log(obj.title);
  }
});
