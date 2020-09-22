#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movieId;
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const charactersInMovies = JSON.parse(body).characters;
    for (const character in charactersInMovies) {
      const charLink = charactersInMovies[character];
      request(charLink, function (err, response, body) {
        if (err) {
          console.log(err);
        } else {
          const currentcharacter = JSON.parse(body);
          console.log(currentcharacter.name);
          console.log(currentcharacter.films);
        }
      });
    }
  }
});
