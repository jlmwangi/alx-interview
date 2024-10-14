#!/usr/bin/node

const request = require('request');

const episode_id = process.argv[2];  // identify the first arg which is supposed to be an int

const arr = [];

// go to the films endpoint, retrieve the characters
request(`https://swapi-api.alx-tools.com/api/films/${ episode_id }/`, function (error, response, body) {
  if (!error && response.statusCode == 200) {
    const films_endpoint = JSON.parse(body);
    const characters = films_endpoint.characters;
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
