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

  // Create an array of promises to fetch character details
  const characterPromises = characters.map((charUrl) => {
    return new Promise((resolve, reject) => {
      request(charUrl, (error, response, body) => {
        if (error) {
          reject(error);
          return;
        }

        if (response.statusCode !== 200) {
          reject(new Error(`Unable to fetch. Status code: ${response.statusCode}`));
          return;
        }

        const charData = JSON.parse(body);
        resolve(charData.name); // Resolve the character's name
      });
    });
  });

  // Wait for all character requests to complete before printing
  Promise.all(characterPromises)
    .then((names) => {
      names.forEach((name) => console.log(name));
    })
    .catch((error) => {
      console.error(error);
    });
});
