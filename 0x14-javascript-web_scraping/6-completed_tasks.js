#!/usr/bin/node

const request = require('request');
const Url = process.argv[2];

if (!Url) {
  console.error('Usage: ./6-completed_tasks.js <API_URL>');
  process.exit(1);
}

request(Url, (error, response, body) => {
  if (error) {
    console.error('Error fetching API:', error);
  }

  if (response.statusCode !== 200) {
    console.error(`Error: Unable to fetch data (Status code: ${response.statusCode})`);
  }

  const todos = JSON.parse(body);
  const completedTasks = {};

  todos.forEach(task => {
    if (task.completed) {
      if (!completedTasks[task.userId]) {
        completedTasks[task.userId] = 0;
      }
      completedTasks[task.userId]++;
    }
  });

  console.log(completedTasks);
});
