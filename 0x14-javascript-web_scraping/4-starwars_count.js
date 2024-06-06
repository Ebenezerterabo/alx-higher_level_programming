#!/usr/bin/node
/* A script that prints the number of movies where the character "Wedge Antilles" is present. */

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
let count = 0;

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(response.body);
    data.results.forEach((movie) => {
      movie.characters.forEach((character) => {
        if (character.includes('18')) {
          count++;
        }
      });
    });
    console.log(count);
  }
});
