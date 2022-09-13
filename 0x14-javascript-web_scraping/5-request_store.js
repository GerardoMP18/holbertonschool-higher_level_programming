#!/usr/bin/node
// script that gets the contents of a webpage and stores it in a file

const endPoint = process.argv[2];
const path = process.argv[3];
const axios = require('axios').default;
const fs = require('fs');

axios.get(endPoint).then(
  (response) => {
    const data = response.data;
    fs.writeFile(path, data, (err) => {
      if (err) {
        console.log(err);
      }
    });
  }).catch(
  (error) => {
    console.log(error);
  });
