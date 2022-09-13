#!/usr/bin/node
// script that prints the number of movies where the character “Wedge Antilles” is present

const endPoint = process.argv[2];
const axios = require('axios').default;

axios.get(endPoint).then(
  (response) => {
    const contador = response.data.results.filter(movies => movies.characters
      .find(characterID => characterID.includes('18')
      )).length;
    console.log(contador);
  }).catch(
  (error) => {
    console.log(error);
  });
