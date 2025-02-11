#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

if (!url) {
  console.log('Usage: ./4-starwars_count.js <URL>');
  process.exit(1);
}

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.log(`Unable to fetch. Status code: ${response.statusCode}`);
    return;
  }

  const data = JSON.parse(body);
  const films = data.results;

  const count = films.filter(film =>
    film.characters.some(characterUrl => characterUrl.includes('/18/'))
  ).length;

  console.log(count);
});
