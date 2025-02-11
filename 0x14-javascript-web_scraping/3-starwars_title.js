#!/usr/bin/node

const request = require('request');

if (process.argv.length > 3) {
  console.log('Usage: ./3-starwars_title <Episode>');
  process.exit(1);
}

const episode = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${episode}`;

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.log(`Failed to fetch data. Status code: ${response.statusCode}`);
    return;
  }

  const data = JSON.parse(body);
  console.log(data.title);
});
