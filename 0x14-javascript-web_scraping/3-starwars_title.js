#!/usr/bin/node
// script that prints the title of a Star Wars movie where the episode number matches a given integer

const movieID = process.argv[2];
const endPoint = 'https://swapi-api.hbtn.io/api/films/' + movieID;
const axios = require('axios').default;

axios.get(endPoint).then(
  (response) => {
    console.log(response.data.title);
  }).catch(
  (error) => {
    console.log(error);
  });
