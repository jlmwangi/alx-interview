#!/usr/bin/node

const request = require('request');

const episodeId = process.argv[2]; // identify the first arg which is supposed to be an int

// go to the films endpoint, retrieve the characters
request(`https://swapi-api.alx-tools.com/api/films/${episodeId}/`, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const filmsEndpoint = JSON.parse(body);
    const characters = filmsEndpoint.characters;
    const fetchCharacters = (urls) => {
      const characterPromises = urls.map(characterUrl => {
        return new Promise((resolve, reject) => {
          request(characterUrl, function (err, resp, charBody) {
            if (!err && resp.statusCode === 200) {
              const charData = JSON.parse(charBody);
              resolve(charData.name);
            } else {
              reject(err);
            }
          });
        });
      });
      return Promise.all(characterPromises);
    };

    fetchCharacters(characters)
      .then(characterNames => {
        characterNames.forEach(name => {
          console.log(name);
        });
      })
      .catch(err => {
        console.error(err);
      });
  } else {
    console.error(error);
  }
});
