#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response) {
    const completedTasks = {};
    const tasks = JSON.parse(body);
    for (const i in tasks) {
      const currentTask = tasks[i];
      if (currentTask.completed === true) {
        if (completedTasks[currentTask.userId] === undefined) {
          completedTasks[currentTask.userId] = 1;
        } else {
          completedTasks[currentTask.userId]++;
        }
      }
    }
    console.log(completedTasks);
  }
});
