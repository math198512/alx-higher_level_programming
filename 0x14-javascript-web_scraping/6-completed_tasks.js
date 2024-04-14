#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error); // Print the error if one occurred
  } else {
    const obj = JSON.parse(body);
    const todoDict = {};

    const numTodos = obj.length;
    for (let i = 0; i < numTodos; i++) {
      const userId = obj[i].userId;
      const completed = obj[i].completed;

      if (completed && !todoDict[userId]) {
        todoDict[userId] = 0;
      }
      if (completed) {
        ++todoDict[userId];
      }
    }
    console.log(todoDict);
  }
});
