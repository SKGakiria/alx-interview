#!/usr/bin/node
const request = require('request');
const movieID = process.argv[2];
const API_URL = `https://swapi-api.hbtn.io/api/films/${movieID}/`;

request(API_URL, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    displayCharacters(characters, 0);
  }
});

function displayCharacters (characters, idx) {
  request(characters[idx], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (idx + 1 < characters.length) {
        displayCharacters(characters, idx + 1);
      }
    }
  });
}
