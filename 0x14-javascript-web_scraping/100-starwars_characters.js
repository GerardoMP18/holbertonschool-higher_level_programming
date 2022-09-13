#!/usr/bin/node
// script that prints all characters of a Star Wars movie

const movieID = process.argv[2];
const endpointFilms = 'https://swapi-api.hbtn.io/api/films/' + movieID;
const axios = require('axios').default;

axios.get(endpointFilms).then(
  (response) => {
    const endpointpeople = response.data.characters;
    endpointpeople.forEach(element => {
      axios.get(element).then(
        (people) => {
          console.log(people.data.name);
        }).catch(
        (err) => {
          console.log(err);
        });
    });
  }).catch(
  (error) => {
    console.log(error);
  });
