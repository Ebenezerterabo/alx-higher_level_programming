#!/usr/bin/node
// A script that computes and prints the number of tasks completed by user id.

const request = require('request');
const url = process.argv[2];
const completed = {};

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    for (const task of data) {
      if (task.completed) {
        if (completed[task.userId]) {
          completed[task.userId]++;
        } else {
          completed[task.userId] = 1;
        }
      }
    }
    console.log(completed);
  }
});
