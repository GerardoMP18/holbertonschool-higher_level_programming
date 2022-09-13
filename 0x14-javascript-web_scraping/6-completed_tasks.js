#!/usr/bin/node
// script that computes the number of tasks completed by user id

const endPoint = process.argv[2];
const axios = require('axios').default;

axios.get(endPoint).then(
  (response) => {
    const myDict = {};
    response.data.forEach(all => {
      if (all.completed === true) {
        if (myDict[all.userId] === undefined) {
          myDict[all.userId] = 1;
        } else {
          myDict[all.userId] += 1;
        }
      }
    });
    console.log(myDict);
  }).catch(
  (error) => {
    console.log(error);
  });
