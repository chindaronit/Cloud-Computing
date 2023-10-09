const express = require('express');
const path = require('path');
const app = express();
const contact= require('./routes/contact')


// Setup static middleware to serve static files from the "public" directory
app.use(express.static(path.join(__dirname, 'views')))
app.use(express.urlencoded({ extended: false }))
app.use(express.json()) // Use express.json() middleware to parse JSON data
app.use('', contact)


app.listen(80, () => {
    console.log("Server is listening on port 80...");
});


