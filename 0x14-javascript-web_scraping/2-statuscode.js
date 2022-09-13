#!/usr/bin/node
// script that display the status code of a GET request

const url = process.argv[2];
const axios = require('axios').default;

axios.get(url)
  .then((response) => {
    console.log('code: ' + response.status);
  }).catch((error) => {
    console.log('code: ' + error.response.status);
  });
