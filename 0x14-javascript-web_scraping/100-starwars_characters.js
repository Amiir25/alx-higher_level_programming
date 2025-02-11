#!/usr/bin/node

const request = require('request');
const filmId = process.argv[2];
const filmUrl = `https://swapi-api.alx-tools.com/api/films/${filmId}`;

if (!filmId) {
  console.log('Usage: ./100-starwars_characters.js <Film ID>');
  process.exit(1);
}

request(filmUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  }

  if (response.statusCode !== 200) {
    console.error(`Unable to fetch. Status code: ${response.statusCode}`);
  }

  const data = JSON.parse(body);
  const characters = data.characters;

  for (const charUrl of characters) {
    request(charUrl, (error, response, body) => {
      if (error) {
        console.error(error);
      }

      if (response.statusCode !== 200) {
        console.error(`Unable to fetch. Status code: ${response.statusCode}`);
      }

      const charData = JSON.parse(body);
      console.log(charData.name);
    });
  }
});
