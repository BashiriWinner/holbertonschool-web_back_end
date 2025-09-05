const express = require('express');

const app = express();
const port = 1245;

// Handler for root route
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

// Handling 404 errors
app.use((req, res) => {
  res.status(404).send('Not Found');
});

// Starting the server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});

module.exports = app;
