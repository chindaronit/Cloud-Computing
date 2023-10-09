const express = require('express');
const path = require('path');
const app = express();
const user= require('./routes/user')

// Setup static middleware to serve static files from the "public" directory
app.use(express.static('public'))
app.use(express.urlencoded({ extended: false }))
app.use(express.json()) // Use express.json() middleware to parse JSON data
app.use('/', user)


app.listen(8001, () => {
    console.log("Server is listening on port 8001...");
});
