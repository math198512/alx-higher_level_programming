#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

request('https://swapi-api.alx-tools.com/api/films/' + movieId, function (error, response, body) {
  if (error) {
    console.error(error); // Print the error if one occurred
  } else {
    const obj = JSON.parse(body);
    const characters = obj.characters;
    for (let i = 0; i < characters.length; i++) {
      request(characters[i], function (error, response, body) {
        if (error) {
          console.error(error);
        } else {
          const character = JSON.parse(body);
          const name = character.name;
          console.log(name);
        }
      });
    }
  }
});
