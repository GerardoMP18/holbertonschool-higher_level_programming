#!/usr/bin/node
const fs = require('fs');
const dataA = fs.readFileSync(process.argv[2], { encoding: 'utf8', flag: 'r' });
const dataB = fs.readFileSync(process.argv[3], { encoding: 'utf8', flag: 'r' });
const dataC = dataA + '\n' + dataB + '\n';
fs.writeFileSync(process.argv[4], dataC, { encoding: 'utf8', flag: 'w' });
